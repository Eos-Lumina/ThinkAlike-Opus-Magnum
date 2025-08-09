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
                                                                                                                                                                                                                  �.��r�x�J_���w�vkI �f��B�B���c=J�K|�T��!u[��5�b�o����5�>" \�?q�
� ���=�0>�1%v����ɷ&p��%%����U^J�K�;�N�kF��' �p���-�|�`�b���� �Џ1q��f-k���i��f�� 7�4M�}v�-��gR��+_�y��T��5"y�7(,����u`��3b_�0W��`L$�1�V�S���͑g��Ik�+�}�����v^#�bB�f2��^��B!�*�Y7���=<nɎs�?�����U�t٧W:́���4��jJi�!!PEX�m����A%/�$�R�fG]�YV؈��,��m�p�y���9���v�o/���ӗ�Ȩͫ�y�zFL��R8E���0Q�XF'��.��&�M-ɢѕ�<�
ez��}�$�ԇԣZ�N�v|xq�_`��i�������f8)Ί��lݢ������B�Kh"`��|eĖF�r"�bXr���WGd)|*�k�C�! $b�D�"i3�f����(أ�����)��p��݀g�	-O"��I�5�Nk�&~��PH0��	~�,��`~�'G����Z�<�~�I�z>�Y��R����,o�t�SH�Q�> Ӯ}NP[��)F(�q?oa��ov~:S�1IH]-u9�"�r�n.�K��y͵[ض�`O��4���s���T����d��-Uݭ�ԉL����u�Z�9�h	p�O�YT��[2��)i�?��с�]�WU�!�b��C��DfW{��*�����=���2�������E�ךMa��|�6�O��R��w�K����s��{.�i�� ������ L�۔kZ�4D%쭏�Jr��ǞLB��\]�Wu��GI�g(� .50�m��*����}�;sŊrC��_j��Ôz��	N�m�t;�5~G�r���0iQ׶?C�S˯^D�9���g�Fk���o��D�NA~�Z��K�B��L�?�;���|��q�>��(.��2&�f�[�ƌ���T$΋q߶F4�0�5�<)ä�7
�E�o�(�ӆ��d
]���8��R	��m3��T�� ߓx␽̋8�6�w1ȸ��^
A��~wp�x�L�۟�t�x�@@����<H@���RM�D/��et��ëjW�܇L3K�M��B�b�hψ��>���lU��!�&3�at�+��N@��U�wG-<86�����m�B����b���7�Г���:x���#ڌ��� 3���O�F�9�.��״2N(V�K�^5b,"(�e抿A�~L����z�o� .��` Ng�?�{���N,�d�^`e��Pe��^�k��BcfY��#�mpA������I��򐢼�du¡o�(�1c�҇��J�|��vb��܄�ۋ�ap���l����d�yI:�ԝ_).�"��(���9fh��HU�h�B����śeB�����Jr��mT��f��:D���Ve���6|�cs$�H3Ǟ�U�3����=�y'pިS#�vhA �Ev7Vg�����
=�p`h.Y�	��3��L�TL��8�v�B�1���y���8�b�Xg
��DDe����u	�	Ș�m>/h8-\K5�ɾ�X/��~_c���uvY���J욗H�����?�|���raǦ��S���n���&�J���p���M��u[QPj�3��l��E��ֶ۞E��م�
#9e̼X�����H��tN/��ĳs���*�\�JagDH�`����a�)�:Pc����7�;N&G���b�rNQZ��r&܉K-�=�������xvn��7����8L�c�#{[$c�iy��엌�����J��K*+�v��o�in��Xq�N��x�r4,�Կ,��<%���2 V�ݗ27���tt�L�ldx�oL�D窙ڢ�i.����~�aԉg�(���F@K'�l|ȟݑRu�h�Ű�~�c%e�s)��{C�8fŏ?|t�[5֖��< ���eq���s`���M�� ~���@V�=t��>7�����3�u�I�7�2�S$�4���vڟ��b��(A���(��b��I�/&�r���~�6R>�K=5��ǿ�Ρ��&΋�n�����e�!�����~8�X�`B̞G��N��ف��i�X�6ʹ�g��H6y���r���;&��3:g�淥>�S.������0��*�[�v��P""0P�T�wgѽ�]�7�����6�ѦR=|���:Mo�OЙ���黊���) �(=��ʃz�N��[�SNX��(�&-�Tɞ����'������yc29x[}�/���gyq�a�)�>R\2�N��Nf�N�2�C���Q�8m�E6"�L^% p��lP��م�� ��°���r�C�^����h�#Y��u�{�?�K��U����s=xfED�R��A���)L�Duy�~Prl����nU�ߒbVy�h����̠Y�8�D��,��M]4�kt�zI�"Bx��(w����p�F8�	��Kp�$���T8̥I�[��!�P�a�jJ�C��ѥĥxrN<��3���TJ"���䳦��E$�FL3�Q�~�q �p�Q&X��cK�h4���dQ 䔆JUp��{ѣ�(g��j7J�F�u�d+�J��b�4�d���C㋶gn������3�C/���rh��<��8�y��lg Q�-<�O�[cm�`��H"4N�3��S@�����`�Z�	Ԉ�8С�%l&�R�^=+&�Q`4�,슐@���P�χ�2(H��