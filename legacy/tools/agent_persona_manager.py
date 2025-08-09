    lArc = disappearing[0];
		          rArc = disappearing[nArcs - 1];
		          rArc.edge = d3_geom_voronoiCreateEdge(lArc.site, rArc.site, null, vertex);
		          d3_geom_voronoiAttachCircle(lArc);
		          d3_geom_voronoiAttachCircle(rArc);
		        }
		        function d3_geom_voronoiAddBeach(site) {
		          var x = site.x, directrix = site.y, lArc, rArc, dxl, dxr, node = d3_geom_voronoiBeaches._;
		          while (node) {
		            dxl = d3_geom_voronoiLeftBreakPoint(node, directrix) - x;
		            if (dxl > \u03B5) node = node.L;
		            else {
		              dxr = x - d3_geom_voronoiRightBreakPoint(node, directrix);
		              if (dxr > \u03B5) {
		                if (!node.R) {
		                  lArc = node;
		                  break;
		                }
		                node = node.R;
		              } else {
		                if (dxl > -\u03B5) {
		                  lArc = node.P;
		                  rArc = node;
		                } else if (dxr > -\u03B5) {
		                  lArc = node;
		                  rArc = node.N;
		                } else {
		                  lArc = rArc = node;
		                }
		                break;
		              }
		            }
		          }
		          var newArc = d3_geom_voronoiCreateBeach(site);
		          d3_geom_voronoiBeaches.insert(lArc, newArc);
		          if (!lArc && !rArc) return;
		          if (lArc === rArc) {
		            d3_geom_voronoiDetachCircle(lArc);
		            rArc = d3_geom_voronoiCreateBeach(lArc.site);
		            d3_geom_voronoiBeaches.insert(newArc, rArc);
		            newArc.edge = rArc.edge = d3_geom_voronoiCreateEdge(lArc.site, newArc.site);
		            d3_geom_voronoiAttachCircle(lArc);
		            d3_geom_voronoiAttachCircle(rArc);
		            return;
		          }
		          if (!rArc) {
		            newArc.edge = d3_geom_voronoiCreateEdge(lArc.site, newArc.site);
		            return;
		          }
		          d3_geom_voronoiDetachCircle(lArc);
		          d3_geom_voronoiDetachCircle(rArc);
		          var lSite = lArc.site, ax = lSite.x, ay = lSite.y, bx = site.x - ax, by = site.y - ay, rSite = rArc.site, cx = rSite.x - ax, cy = rSite.y - ay, d = 2 * (bx * cy - by * cx), hb = bx * bx + by * by, hc = cx * cx + cy * cy, vertex = {
		            x: (cy * hb - by * hc) / d + ax,
		            y: (bx * hc - cx * hb) / d + ay
		          };
		          d3_geom_voronoiSetEdgeEnd(rArc.edge, lSite, rSite, vertex);
		          newArc.edge = d3_geom_voronoiCreateEdge(lSite, site, null, vertex);
		          rArc.edge = d3_geom_voronoiCreateEdge(site, rSite, null, vertex);
		          d3_geom_voronoiAttachCircle(lArc);
		          d3_geom_voronoiAttachCircle(rArc);
		        }
		        function d3_geom_voronoiLeftBreakPoint(arc, directrix) {
		          var site = arc.site, rfocx = site.x, rfocy = site.y, pby2 = rfocy - directrix;
		          if (!pby2) return rfocx;
		          var lArc = arc.P;
		          if (!lArc) return -Infinity;
		          site = lArc.site;
		          var lfocx = site.x, lfocy = site.y, plby2 = lfocy - directrix;
		          if (!plby2) return lfocx;
		          var hl = lfocx - rfocx, aby2 = 1 / pby2 - 1 / plby2, b = hl / plby2;
		          if (aby2) return (-b + Math.sqrt(b * b - 2 * aby2 * (hl * hl / (-2 * plby2) - lfocy + plby2 / 2 + rfocy - pby2 / 2))) / aby2 + rfocx;
		          return (rfocx + lfocx) / 2;
		        }
		        function d3_geom_voronoiRightBreakPoint(arc, directrix) {
		          var rArc = arc.N;
		          if (rArc) return d3_geom_voronoiLeftBreakPoint(rArc, directrix);
		          var site = arc.site;
		          return site.y === directrix ? site.x : Infinity;
		        }
		        function d3_geom_voronoiCell(site) {
		          this.site = site;
		          this.edges = [];
		        }
		        d3_geom_voronoiCell.prototype.prepare = function() {
		          var halfEdges = this.edges, iHalfEdge = halfEdges.length, edge;
		          while (iHalfEdge--) {
		            edge = halfEdges[iHalfEdge].edge;
		            if (!edge.b || !edge.a) halfEdges.splice(iHalfEdge, 1);
		          }
		          halfEdges.sort(d3_geom_voronoiHalfEdgeOrder);
		          return halfEdges.length;
		        };
		        function d3_geom_voronoiCloseCells(extent) {
		          var x0 = extent[0][0], x1 = extent[1][0], y0 = extent[0][1], y1 = extent[1][1], x2, y2, x3, y3, cells = d3_geom_voronoiCells, iCell = cells.length, cell, iHalfEdge, halfEdges, nHalfEdges, start, end;
		          while (iCell--) {
		            cell = cells[iCell];
		            if (!cell || !cell.prepare()) continue;
		            halfEdges = cell.edges;
		            nHalfEdges = halfEdges.length;
		            iHalfEdge = 0;
		            while (iHalfEdge < nHalfEdges) {
		              end = halfEdges[iHalfEdge].end(), x3 = end.x, y3 = end.y;
		              start = halfEdges[++iHalfEdge % nHalfEdges].start(), x2 = start.x, y2 = start.y;
		              if (abs(x3 - x2) > \u03B5 || abs(y3 - y2) > \u03B5) {
		                halfEdges.splice(iHalfEdge, 0, new d3_geom_voronoiHalfEdge(d3_geom_voronoiCreateBorderEdge(cell.site, end, abs(x3 - x0) < \u03B5 && y1 - y3 > \u03B5 ? {
		                  x: x0,
		                  y: abs(x2 - x0) < \u03B5 ? y2 : y1
		                } : abs(y3 - y1) < \u03B5 && x1 - x3 > \u03B5 ? {
		                  x: abs(y2 - y1) < \u03B5 ? x2 : x1,
		                  y: y1
		                } : abs(x3 - x1) < \u03B5 && y3 - y0 > \u03B5 ? {
		                  x: x1,
		                  y: abs(x2 - x1) < \u03B5 ? y2 : y0
		                } : abs(y3 - y0) < \u03B5 && x3 - x0 > \u03B5 ? {
		                  x: abs(y2 - y0) < \u03B5 ? x2 : x0,
		                  y: y0
		                } : null), cell.site, null));
		                ++nHalfEdges;
		              }
		            }
		          }
		        }
		        function d3_geom_voronoiHalfEdgeOrder(a, b) {
		          return b.angle - a.angle;
		        }
		        function d3_geom_voronoiCircle() {
		          d3_geom_voronoiRedBlackNode(this);
		          this.x = this.y = this.arc = this.site = this.cy = null;
		        }
		        function d3_geom_voronoiAttachCircle(arc) {
		          var lArc = arc.P, rArc = arc.N;
		          if (!lArc || !rArc) return;
		          var lSite = lArc.site, cSite = arc.site, rSite = rArc.site;
		          if (lSite === rSite) return;
		          var bx = cSite.x, by = cSite.y, ax = lSite.x - bx, ay = lSite.y - by, cx = rSite.x - bx, cy = rSite.y - by;
		          var d = 2 * (ax * cy - ay * cx);
		          if (d >= -\u03B52) return;
		          var ha = ax * ax + ay * ay, hc = cx * cx + cy * cy, x = (cy * ha - ay * hc) / d, y = (ax * hc - cx * ha) / d, cy = y + by;
		          var circle = d3_geom_voronoiCirclePool.pop() || new d3_geom_voronoiCircle();
		          circle.arc = arc;
		          circle.site = cSite;
		          circle.x = x + bx;
		          circle.y = cy + Math.sqrt(x * x + y * y);
		          circle.cy = cy;
		          arc.circle = circle;
		          var before = null, node = d3_geom_voronoiCircles._;
		          while (node) {
		            if (circle.y < node.y || circle.y === node.y && circle.x <= node.x) {
		              if (node.L) node = node.L;
		              else {
		                before = node.P;
		                break;
		              }
		            } else {
		              if (node.R) node = node.R;
		              else {
		                before = node;
		                break;
		              }
		            }
		          }
		          d3_geom_voronoiCircles.insert(before, circle);
		          if (!before) d3_geom_voronoiFirstCircle = circle;
		        }
		        function d3_geom_voronoiDetachCircle(arc) {
		          var circle = arc.circle;
		          if (circle) {
		            if (!circle.P) d3_geom_voronoiFirstCircle = circle.N;
		            d3_geom_voronoiCircles.remove(circle);
		            d3_geom_voronoiCirclePool.push(circle);
		            d3_geom_voronoiRedBlackNode(circle);
		            arc.circle = null;
		          }
		        }
		        function d3_geom_clipLine(x0, y0, x1, y1) {
		          return function(line) {
		            var a = line.a, b = line.b, ax = a.x, ay = a.y, bx = b.x, by = b.y, t0 = 0, t1 = 1, dx = bx - ax, dy = by - ay, r;
		            r = x0 - ax;
		            if (!dx && r > 0) return;
		            r /= dx;
		            if (dx < 0) {
		              if (r < t0) return;
		              if (r < t1) t1 = r;
		            } else if (dx > 0) {
		              if (r > t1) return;
		              if (r > t0) t0 = r;
		            }
		            r = x1 - ax;
		            if (!dx && r < 0) return;
		            r /= dx;
		            if (dx < 0) {
		              if (r > t1) return;
		              if (r > t0) t0 = r;
		            } else if (dx > 0) {
		              if (r < t0) return;
		              if (r < t1) t1 = r;
		            }
		            r = y0 - ay;
		            if (!dy && r > 0) return;
		            r /= dy;
		            if (dy < 0) {
		              if (r < t0) return;
		              if (r < t1) t1 = r;
		            } else if (dy > 0) {
		              if (r > t1) return;
		              if (r > t0) t0 = r;
		            }
		            r = y1 - ay;
		            if (!dy && r < 0) return;
		            r /= dy;
		            if (dy < 0) {
		              if (r > t1) return;
		              if (r > t0) t0 = r;
		            } else if (dy > 0) {
		              if (r < t0) return;
		              if (r < t1) t1 = r;
		            }
		            if (t0 > 0) line.a = {
		              x: ax + t0 * dx,
		              y: ay + t0 * dy
		            };
		            if (t1 < 1) line.b = {
		              x: ax + t1 * dx,
		              y: ay + t1 * dy
		            };
		            return line;
		          };
		        }
		        function d3_geom_voronoiClipEdges(extent) {
		          var edges = d3_geom_voronoiEdges, clip = d3_geom_clipLine(extent[0][0], extent[0][1], extent[1][0], extent[1][1]), i = edges.length, e;
		          while (i--) {
		            e = edges[i];
		            if (!d3_geom_voronoiConnectEdge(e, extent) || !clip(e) || abs(e.a.x - e.b.x) < \u03B5 && abs(e.a.y - e.b.y) < \u03B5) {
		              e.a = e.b = null;
		              edges.splice(i, 1);
		            }
		          }
		        }
		        functio