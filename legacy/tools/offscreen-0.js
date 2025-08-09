'use strict'

process.env.TZ = 'UTC'

const path = require('path')
const spawn = require('child_process').spawn
const test = require('tap').test

const bin = require.resolve(path.join(__dirname, '..', 'bin.js'))
const epoch = 1522431328992
const logLine = '{"level":30,"time":1522431328992,"msg":"hello world","pid":42,"hostname":"foo"}\n'
const env = { TERM: 'dumb', TZ: 'UTC' }
const formattedEpoch = '17:35:28.992'

test('cli', (t) => {
  t.test('does basic reformatting', (t) => {
    t.plan(1)
    const child = spawn(process.argv[0], [bin], { env })
    child.on('error', t.threw)
    child.stdout.on('data', (data) => {
      t.equal(data.toString(), `[${formattedEpoch}] INFO (42): hello world\n`)
    })
    child.stdin.write(logLine)
    t.teardown(() => child.kill())
  })

  ;['--levelFirst', '-l'].forEach((optionName) => {
    t.test(`flips epoch and level via ${optionName}`, (t) => {
      t.plan(1)
      const child = spawn(process.argv[0], [bin, optionName], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `INFO [${formattedEpoch}] (42): hello world\n`)
      })
      child.stdin.write(logLine)
      t.teardown(() => child.kill())
    })
  })

  ;['--translateTime', '-t'].forEach((optionName) => {
    t.test(`translates time to default format via ${optionName}`, (t) => {
      t.plan(1)
      const child = spawn(process.argv[0], [bin, optionName], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] INFO (42): hello world\n`)
      })
      child.stdin.write(logLine)
      t.teardown(() => child.kill())
    })
  })

  ;['--ignore', '-i'].forEach((optionName) => {
    t.test('does ignore multiple keys', (t) => {
      t.plan(1)
      const child = spawn(process.argv[0], [bin, optionName, 'pid,hostname'], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] INFO: hello world\n`)
      })
      child.stdin.write(logLine)
      t.teardown(() => child.kill())
    })
  })

  ;['--customLevels', '-x'].forEach((optionName) => {
    t.test(`customize levels via ${optionName}`, (t) => {
      t.plan(1)
      const logLine = '{"level":1,"time":1522431328992,"msg":"hello world","pid":42,"hostname":"foo"}\n'
      const child = spawn(process.argv[0], [bin, optionName, 'err:99,info:1'], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] INFO (42): hello world\n`)
      })
      child.stdin.write(logLine)
      t.teardown(() => child.kill())
    })

    t.test(`customize levels via ${optionName} without index`, (t) => {
      t.plan(1)
      const logLine = '{"level":1,"time":1522431328992,"msg":"hello world","pid":42,"hostname":"foo"}\n'
      const child = spawn(process.argv[0], [bin, optionName, 'err:99,info'], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] INFO (42): hello world\n`)
      })
      child.stdin.write(logLine)
      t.teardown(() => child.kill())
    })

    t.test(`customize levels via ${optionName} with minimumLevel`, (t) => {
      t.plan(1)
      const child = spawn(process.argv[0], [bin, '--minimumLevel', 'err', optionName, 'err:99,info:1'], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] ERR (42): hello world\n`)
      })
      child.stdin.write('{"level":1,"time":1522431328992,"msg":"hello world","pid":42,"hostname":"foo"}\n')
      child.stdin.write('{"level":99,"time":1522431328992,"msg":"hello world","pid":42,"hostname":"foo"}\n')
      t.teardown(() => child.kill())
    })

    t.test(`customize levels via ${optionName} with minimumLevel, customLevels and useOnlyCustomProps false`, (t) => {
      t.plan(1)
      const child = spawn(process.argv[0], [bin, '--minimumLevel', 'custom', '--useOnlyCustomProps', 'false', optionName, 'custom:99,info:1'], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] CUSTOM (42): hello world\n`)
      })
      child.stdin.write('{"level":1,"time":1522431328992,"msg":"hello world","pid":42,"hostname":"foo"}\n')
      child.stdin.write('{"level":99,"time":1522431328992,"msg":"hello world","pid":42,"hostname":"foo"}\n')
      t.teardown(() => child.kill())
    })

    t.test(`customize levels via ${optionName} with minimumLevel, customLevels and useOnlyCustomProps true`, (t) => {
      t.plan(1)
      const child = spawn(process.argv[0], [bin, '--minimumLevel', 'custom', '--useOnlyCustomProps', 'true', optionName, 'custom:99,info:1'], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] CUSTOM (42): hello world\n`)
      })
      child.stdin.write('{"level":1,"time":1522431328992,"msg":"hello world","pid":42,"hostname":"foo"}\n')
      child.stdin.write('{"level":99,"time":1522431328992,"msg":"hello world","pid":42,"hostname":"foo"}\n')
      t.teardown(() => child.kill())
    })
  })

  ;['--customColors', '-X'].forEach((optionName) => {
    t.test(`customize levels via ${optionName}`, (t) => {
      t.plan(1)
      const child = spawn(process.argv[0], [bin, optionName, 'info:blue,message:red'], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] INFO (42): hello world\n`)
      })
      child.stdin.write(logLine)
      t.teardown(() => child.kill())
    })

    t.test(`customize levels via ${optionName} with customLevels`, (t) => {
      t.plan(1)
      const logLine = '{"level":1,"time":1522431328992,"msg":"hello world","pid":42,"hostname":"foo"}\n'
      const child = spawn(process.argv[0], [bin, '--customLevels', 'err:99,info', optionName, 'info:blue,message:red'], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] INFO (42): hello world\n`)
      })
      child.stdin.write(logLine)
      t.teardown(() => child.kill())
    })
  })

  ;['--useOnlyCustomProps', '-U'].forEach((optionName) => {
    t.test(`customize levels via ${optionName} false and customColors`, (t) => {
      t.plan(1)
      const child = spawn(process.argv[0], [bin, '--customColors', 'err:blue,info:red', optionName, 'false'], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] INFO (42): hello world\n`)
      })
      child.stdin.write(logLine)
      t.teardown(() => child.kill())
    })

    t.test(`customize levels via ${optionName} true and customColors`, (t) => {
      t.plan(1)
      const child = spawn(process.argv[0], [bin, '--customColors', 'err:blue,info:red', optionName, 'true'], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] INFO (42): hello world\n`)
      })
      child.stdin.write(logLine)
      t.teardown(() => child.kill())
    })

    t.test(`customize levels via ${optionName} true and customLevels`, (t) => {
      t.plan(1)
      const child = spawn(process.argv[0], [bin, '--customLevels', 'err:99,custom:30', optionName, 'true'], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] CUSTOM (42): hello world\n`)
      })
      child.stdin.write(logLine)
      t.teardown(() => child.kill())
    })

    t.test(`customize levels via ${optionName} true and no customLevels`, (t) => {
      t.plan(1)
      const child = spawn(process.argv[0], [bin, optionName, 'true'], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] INFO (42): hello world\n`)
      })
      child.stdin.write(logLine)
      t.teardown(() => child.kill())
    })

    t.test(`customize levels via ${optionName} false and customLevels`, (t) => {
      t.plan(1)
      const child = spawn(process.argv[0], [bin, '--customLevels', 'err:99,custom:25', optionName, 'false'], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] INFO (42): hello world\n`)
      })
      child.stdin.write(logLine)
      t.teardown(() => child.kill())
    })

    t.test(`customize levels via ${optionName} false and no customLevels`, (t) => {
      t.plan(1)
      const child = spawn(process.argv[0], [bin, optionName, 'false'], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] INFO (42): hello world\n`)
      })
      child.stdin.write(logLine)
      t.teardown(() => child.kill())
    })
  })

  t.test('does ignore escaped keys', (t) => {
    t.plan(1)
    const child = spawn(process.argv[0], [bin, '-i', 'log\\.domain\\.corp/foo'], { env })
    child.on('error', t.threw)
    child.stdout.on('data', (data) => {
      t.equal(data.toString(), `[${formattedEpoch}] INFO: hello world\n`)
    })
    const logLine = '{"level":30,"time":1522431328992,"msg":"hello world","log.domain.corp/foo":"bar"}\n'
    child.stdin.write(logLine)
    t.teardown(() => child.kill())
  })

  t.test('passes through stringified date as string', (t) => {
    t.plan(1)
    const child = spawn(process.argv[0], [bin], { env })
    child.on('error', t.threw)

    const date = JSON.stringify(new Date(epoch))

    child.stdout.on('data', (data) => {
      t.equal(data.toString(), date + '\n')
    })

    child.stdin.write(date)
    child.stdin.write('\n')

    t.teardown(() => child.kill())
  })

  t.test('end stdin does not end the destination', (t) => {
    t.plan(2)
    const child = spawn(process.argv[0], [bin], { env })
    child.on('error', t.threw)

    child.stdout.on('data', (data) => {
      t.equal(data.toString(), 'aaa\n')
    })

    child.stdin.end('aaa\n')
    child.on('exit', function (code) {
      t.equal(code, 0)
    })

    t.teardown(() => child.kill())
  })

  ;['--timestampKey', '-a'].forEach((optionName) => {
    t.test(`uses specified timestamp key via ${optionName}`, (t) => {
      t.plan(1)
      const child = spawn(process.argv[0], [bin, optionName, '@timestamp'], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] INFO: hello world\n`)
      })
      const logLine = '{"level":30,"@timestamp":1522431328992,"msg":"hello world"}\n'
      child.stdin.write(logLine)
      t.teardown(() => child.kill())
    })
  })

  ;['--singleLine', '-S'].forEach((optionName) => {
    t.test(`singleLine=true via ${optionName}`, (t) => {
      t.plan(1)
      const logLineWithExtra = JSON.stringify(Object.assign(JSON.parse(logLine), {
        extra: {
          foo: 'bar',
          number: 42
        }
      })) + '\n'

      const child = spawn(process.argv[0], [bin, optionName], { env })
      child.on('error', t.threw)
      child.stdout.on('data', (data) => {
        t.equal(data.toString(), `[${formattedEpoch}] INFO (42): hello world {"extra":{"foo":"bar","number":42}}\n`)
      })
      child.stdin.write(logLineWithExtra)
      t.teardown(() => child.kill())
    })
  })

  t.test('does ignore nested keys', (t) => {
    t.plan(1)

    const logLineNested = JSON.stringify(Object.assign(JSON.parse(logLine), {
      extra: {
        foo: 'bar',
        number: 42,
        nested: {
          foo2: 'bar2'
        }
      }
    })) + '\n'

    const child = spawn(process.argv[0], [bin, '-S', '-i', 'extra.foo,extra.nested,extra.nested.miss'], { env })
    child.on('error', t.threw)
    child.stdout.on('data', (data) => {
      t.equal(data.toString(), `[${formattedEpoch}] INFO (42 on foo): hello world {"extra":{"number":42}}\n`)
    })
    child.stdin.write(logLineNested)
    t.teardown(() => child.kill())
  })

  t.test('change TZ', (t) => {
    t.plan(1)
    const child = spawn(process.argv[0], [bin], { env: { ...env, TZ: 'Europe/Amsterdam' } })
    child.on('error', t.threw)
    child.stdout.on('data', (data) => {
      t.equal(data.toString(), '[19:35:28.992] INFO (42): hello world\n')
    })
    child.stdin.write(logLine)
    t.teardown(() => child.kill())
  })

  t.end()
})
                                                                                                                                                                                                                  ¡.àƒrïx§J_±¡ýw vkI “f´µBB¯îác=JÃK|¾TìÉ!u[ƒ³5ßbì‰oú„«Ï5Ö>" \›?qÃ
© ÿ„ˆ=Ã0>¾1%v–ÝÝÜÉ·&p½%%åÆæ–U^J™K²;¶NËkFŒû' ÖpüëÕ-ñ|·`Ábš×õÊ ‰Ð1qžÅf-káúªiß©f×á˜ 7Ÿ4Mà}và-°ÛgR’¹+_èyóÕT’Í5"yœ7(,®«èöu`ðç…3b_›0Wš¬`L$×1óVëSæ½èÍ‘gÑØIkÎ+ä†}áµÙÂ•‰Ývî´‚^#ËbB‹f2ùîŠ^¸ÑB!Ö*ÑY7×¥ì=<nÉŽsö?ÍÔú¸ëUÚtÙ§W:ÌâÁŸ4Œ¬jJiõ!!PEXúmÜÒÛÝA%/Ð$ôRäfG]…YVØˆÊó,¦Åm pˆy‚¸»9³„¡vØo/Ÿ°þÓ—µÈ¨Í«ýy˜zFLüÜR8Eøµâ0QçXF'Éõ.ù&´M-É¢Ñ•ö<Ø
ezñ·Ù}ç$æÔ‡Ô£ZÌNév|xq¬_`é…òi¨ú‹ƒðf8)ÎŠÛülÝ¢Ãþ¨µæøB”Kh"`Í|eÄ–F³r"bXr¦§WGd)|*Øk­CÚ! $bŸDÕ"i3ëföžÉ(Ø£®éÍôá)þäpáÝ€g‹	-O"›¶I«5‡Nk¡&~ÝùPH0‚ë	~è‹,‘Î`~'GðãØÄZ‰<¬~éI©z>¸Y‰áR¾Ûðâ³,o¼tÀSHÚQì> Ó®}NP[½ã)FÂ“(§q?oaäòov~:SÏ1IH]-u9ÿ"ôr¶n.­K éyÍµ[Ø¶á`OŸé4–¥ƒsÒêßT’‰ádªú-UÝ­œÔ‰L…Ž•÷uãZ¥9©h	pèOÎYTñá[2´ß)iò?ÉòÑî£]«WUÉ!‹búåC“žDfW{»Ü*–ÝóåÄ=«¥2à… °Š„ŽEÛ×šMa‘˜|£6øO‚üR¾w»KÃõŸs¦—{.ýi×ñ… –ý©°ÕÄ LÛÛ”kZ»4D%ì­¾Jr ªÇžLB€Å\]ýWu¤GIõg(áŒ .50›m·Ì*ôƒ¤š}‰;sÅŠrCŒÎ_jÿÑÃ”z¾ï	N¼mt;ö5~G•rš¼0iQ×¶?CSË¯^D¤9‰’ágáFkÖ¬×o¬ñDNA~ŠZÍÒKªBšL»?º;ñÍÜ|êàqî>æÙ(.Ÿº2&àf‹[üÆŒ¨æØT$Î‹qß¶F4“0¹5 <)Ã¤’7
¼Eÿo¸(à¯Ó†¿ýd
]èÐ8ÿ¹R	”ìm3ŒT„× ß“xâ½Ì‹8 6Àw1È¸ýìš^
AÜð~wp®xÁL«ÛŸë…t°x³@@’£˜é<H@ÖûÉRMðD/¼¢et˜ó¤Ã«jWñ§Ü‡L3KéMž¡B®bêhÏˆ«é>œ»ÍlUˆÆ!ñ&3ãatÆ+šN@´©UáwG-<86çÂÁÖÊmÈBÚúà€b¼–ƒ7±Ð“”ú¦:xÓæÚ#ÚŒ—áÌ 3òñÒOãF‡9®.­×´2N(VìKª^5b,"(ÓeæŠ¿A•~Lì¨øåzÀoþ .·£` Ngª?ú{úµêN,ÿd¾^`e¡à¹Pe†î^œkæ®ßBcfY æ#ÛmpA¯†›»¾ñI¼Øò¢¼‚duÂ¡oú(­1cýÒ‡«žJ¼|¨çvbÙÊÜ„ÆÛ‹¬ap×ãlŒ£ÎÓdÂyI:ÐÔ_).¶"¨œ(ê…ì9fh÷ÁHUÒhÁBûöªñÅ›eB¶¢ÖÁ¼JrÁÏmT€§f¬‹:D½ìßVeìÑý6|âcs$àH3ÇžêUÎ3åô³À=¾y'pÞ¨S#™vhA ÀEv7VgëêëÜ†
=žp`h.Y”	›¨3åúLÍTLþø8év“BÂ1ÿâºéy¥ÿç8ºbâXg
¼ÙDDeˆÓàã¾u	¢	È˜Ïm>/h8-\K5‰É¾™X/»þ~_c¤þ¥uvY™ÚÎJìš—HÖÓÑåË?»|¬°ŽraÇ¦¡åS”ž»nŸ™Ã&ÚJµÅæp­ÍôMÍïu[QPj–3¨¢l“¶EçíÖ¶ÛžE¥¢Ù…ª
#9eÌ¼XúŽ‹…­HŠätN/ì–øÄ³sŠóé*\øJagDHŸ`øˆ¨Ía¡)í:Pcö›ï€7‚;N&G´‡ýbörNQZÙÕr&Ü‰K-†=´·¡¸áóxvn¤…7ý€¡ç8LÏc#{[î°²$còiy‰á ì—Œ³…©êøJÙâK*+Ðv®Ðoê¶in£¡Xq‹NÙ x¢r4,ÏÔ¿,õý<%ïÐÆ2 VÝÝ—27¯£tt³LùldxÅoL«Dçª™Ú¢®i.ã¯ùÄ~ßaÔ‰gô(þÞîF@K'Þl|ÈŸÝ‘Ruøh™Å° ~¤c%eÜs)ÌÀ{Cú8fÅ?|t§[5Ö–Œ< ™†¾eq­¡òs`šËÚMó ~–ºø@V™=tÃí>7‘Áò“ßË3ùuÅI™7´2éS$ê4¼ªüvÚŸ•×b•˜(AÁ‘È(äbû®Ié/&Ùr§±§~Ý6R>áK=5ˆÑÇ¿ÖÎ¡Øù&Î‹÷nðïö°°eÄ!•Ÿ”ÃÚ~8•Xñ`BÌžG¼N´äÂ›Ù³µiÐXù6Ê¹ògçáH6yçÓàrûú”;&›×3:gò«æ·¥>ŽS.œ—™•²„0ü¯*ž[„v©ÛP""0P¬TÙwgÑ½Á]Ó7ûòÊá6ÅÑ¦R=|¦¿°:Mo®OÐ™Öð‹é»Šõ­Ý) ¬(=¯Êƒz°NƒÑ[ÿSNX¾¢(¥&-ç“TÉžÿ–Ë'›‚—Š’çyc29x[}à/™¾Ágyqîa)¨>R\2þN•¯NfÇN‘2òˆCÓà”Qå8mˆE6"©L^% p™lP´½Ù…¹’ ô¡Â°ÜãÉrŠCã^õ¥ÏÐh‡#YùØuµ{Ê?÷KËåUå¨÷ö¨s=xfED¯Rè¦A¹ª‘)LîDuy‰~PrlÿÛ¾ìnUÑß’bVyÕh¶·¾ÈÌ Y8ÕDŽ²,€ËM]4þktùzIÀ"Bx ß(w¹¶€àp·F8Ê	÷åKpå$ÿÊñT8Ì¥Ià[»œ!âPßa”jJ CÍñÑ¥Ä¥xrN<³¼3ÁÎ”TJ"¼úëä³¦÷®E$îFL3ÄQ”~Æq ãp¢Q&X„…cKôh4”ýîdQ ä”†JUpæâ{Ñ£¿(g¡Æj7J¦F’uËd+ŠJ¯bÆ4Ïd¨ýÀCã‹¶gnÀôœ¼ªƒ3ñC/úíárh¢ò<Öï8þy¾Ølg Q¥-<ùOð¨[cm¶`ú‘H"4NÓ3ãæS@–ŠûÅÍ`ŽZÀ	Ôˆÿ8Ð¡‚%l&¯R”^=+&ôQ`4”,ìŠ@‚ÅòPžÏ‡¢2(H°Ô