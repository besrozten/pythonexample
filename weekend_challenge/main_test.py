import unittest
from main import encrypt, decrypt


class Test(unittest.TestCase):

    def test_encrypt(self):
        for i, key in enumerate(self.keys):
            for case in self.cases[i]:
                self.assertEqual(encrypt(case["plain"], key), case["encrypted"])

    def test_decrypt(self):
        for i, key in enumerate(self.keys):
            for case in self.cases[i]:
                self.assertEqual(decrypt(case["encrypted"], key), case["plain"])

    def test_enc_dec_from_file(self):
        testFile = open('test_data.txt', 'r')
        lines = testFile.readlines()
        testFile.close()
        for l in lines:
            self.assertEqual(decrypt(encrypt(l[:-1], 0), 0), l[:-1])
            self.assertEqual(decrypt(encrypt(l[:-1], 10), 10), l[:-1])
            self.assertEqual(decrypt(encrypt(l[:-1], 94), 94), l[:-1])
            self.assertEqual(decrypt(encrypt(l[:-1], 95), 95), l[:-1])
            self.assertEqual(decrypt(encrypt(l[:-1], 96), 96), l[:-1])
            self.assertEqual(decrypt(encrypt(l[:-1], 125), 125), l[:-1])
            self.assertEqual(decrypt(encrypt(l[:-1], 126), 126), l[:-1])
            self.assertEqual(decrypt(encrypt(l[:-1], 127), 127), l[:-1])
            self.assertEqual(decrypt(encrypt(l[:-1], 238), 238), l[:-1])
            self.assertEqual(decrypt(encrypt(l[:-1], 752), 752), l[:-1])
            self.assertEqual(decrypt(encrypt(l[:-1], -10), -10), l[:-1])

    keys = [0, 10, 94, 95, 96, 125, 126, 127, 238, 252, -10]
    cases = [
        [
            {"plain": "Mohamed Salah",
             "encrypted": "Mohamed Salah"
             },
            {"plain": "scored his 22nd",
             "encrypted": "scored his 22nd"
             },
            {"plain": "League leaders Manchester",
             "encrypted": "League leaders Manchester"
             },
            {"plain": "over Newcastle.",
             "encrypted": "over Newcastle."
             },
            {"plain": "12466215376numbers{0!.,;:'^^%///(]=]{}\"'`",
             "encrypted": "12466215376numbers{0!.,;:'^^%///(]=]{}\"'`"
             },
        ],
        [
            {"plain": "Mohamed Salah",
             "encrypted": "Wyrkwon*]kvkr"
             },
            {"plain": "scored his 22nd",
             "encrypted": "}my|on*rs}*<<xn"
             },
            {"plain": "League leaders Manchester",
             "encrypted": "Vokq o*vokno|}*Wkxmro}~o|"
             },
            {"plain": "over Newcastle.",
             "encrypted": "y!o|*Xo\"mk}~vo8"
             },
            {"plain": "12466215376numbers{0!.,;:'^^%///(]=]{}\"'`",
             "encrypted": ";<>@@<;?=A@x wlo|}&:+86ED1hh/9992gGg&(,1j"
             },
        ],
        [
            {"plain": "Mohamed Salah",
             "encrypted": "Lng`ldc~R`k`g"
             },
            {"plain": "scored his 22nd",
             "encrypted": "rbnqdc~ghr~11mc"
             },
            {"plain": "League leaders Manchester",
             "encrypted": "Kd`ftd~kd`cdqr~L`mbgdrsdq"
             },
            {"plain": "over Newcastle.",
             "encrypted": "nudq~Mdvb`rskd-"
             },
            {"plain": "12466215376numbers{0!.,;:'^^%///(]=]{}\"'`",
             "encrypted": "01355104265mtladqrz/ -+:9&]]$...'\\<\\z|!&_"
             },
        ],
        [
            {"plain": "Mohamed Salah",
             "encrypted": "Mohamed Salah"
             },
            {"plain": "scored his 22nd",
             "encrypted": "scored his 22nd"
             },
            {"plain": "League leaders Manchester",
             "encrypted": "League leaders Manchester"
             },
            {"plain": "over Newcastle.",
             "encrypted": "over Newcastle."
             },
            {"plain": "12466215376numbers{0!.,;:'^^%///(]=]{}\"'`",
             "encrypted": "12466215376numbers{0!.,;:'^^%///(]=]{}\"'`"
             },
        ],
        [
            {"plain": "Mohamed Salah",
             "encrypted": "Npibnfe!Tbmbi"
             },
            {"plain": "scored his 22nd",
             "encrypted": "tdpsfe!ijt!33oe"
             },
            {"plain": "League leaders Manchester",
             "encrypted": "Mfbhvf!mfbefst!Nbodiftufs"
             },
            {"plain": "over Newcastle.",
             "encrypted": "pwfs!Ofxdbtumf/"
             },
            {"plain": "12466215376numbers{0!.,;:'^^%///(]=]{}\"'`",
             "encrypted": "23577326487ovncfst|1\"/-<;(__&000)^>^|~#(a"
             },
        ],
        [
            {"plain": "Mohamed Salah",
             "encrypted": "k.' ,$#>q + '"
             },
            {"plain": "scored his 22nd",
             "encrypted": "2\".1$#>'(2>PP-#"
             },
            {"plain": "League leaders Manchester",
             "encrypted": "j$ &4$>+$ #$12>k -\"'$23$1"
             },
            {"plain": "over Newcastle.",
             "encrypted": ".5$1>l$6\" 23+$L"
             },
            {"plain": "12466215376numbers{0!.,;:'^^%///(]=]{}\"'`",
             "encrypted": "OPRTTPOSQUT-4,!$12:N?LJYXE||CMMMF{[{:<@E~"
             },
        ],
        [
            {"plain": "Mohamed Salah",
             "encrypted": "l/(!-%$?r!,!("
             },
            {"plain": "scored his 22nd",
             "encrypted": "3#/2%$?()3?QQ.$"
             },
            {"plain": "League leaders Manchester",
             "encrypted": "k%!'5%?,%!$%23?l!.#(%34%2"
             },
            {"plain": "over Newcastle.",
             "encrypted": "/6%2?m%7#!34,%M"
             },
            {"plain": "12466215376numbers{0!.,;:'^^%///(]=]{}\"'`",
             "encrypted": "PQSUUQPTRVU.5-\"%23;O@MKZYF}}DNNNG|\\|;=AF "
             },
        ],
        [
            {"plain": "Mohamed Salah",
             "encrypted": "m0)\".&%@s\"-\")"
             },
            {"plain": "scored his 22nd",
             "encrypted": "4$03&%@)*4@RR/%"
             },
            {"plain": "League leaders Manchester",
             "encrypted": "l&\"(6&@-&\"%&34@m\"/$)&45&3"
             },
            {"plain": "over Newcastle.",
             "encrypted": "07&3@n&8$\"45-&N"
             },
            {"plain": "12466215376numbers{0!.,;:'^^%///(]=]{}\"'`",
             "encrypted": "QRTVVRQUSWV/6.#&34<PANL[ZG~~EOOOH}]}<>BG!"
             },
        ],
        [
            {"plain": "Mohamed Salah",
             "encrypted": "}@92>65P$2=29"
             },
            {"plain": "scored his 22nd",
             "encrypted": "D4@C65P9:DPbb?5"
             },
            {"plain": "League leaders Manchester",
             "encrypted": "|628F6P=6256CDP}2?496DE6C"
             },
            {"plain": "over Newcastle.",
             "encrypted": "@G6CP~6H42DE=6^"
             },
            {"plain": "12466215376numbers{0!.,;:'^^%///(]=]{}\"'`",
             "encrypted": "abdffbaecgf?F>36CDL`Q^\\kjW//U___X.m.LNRW1"
             },
        ],
        [
            {"plain": "Mohamed Salah",
             "encrypted": ",NG@LDC^2@K@G"
             },
            {"plain": "scored his 22nd",
             "encrypted": "RBNQDC^GHR^ppMC"
             },
            {"plain": "League leaders Manchester",
             "encrypted": "+D@FTD^KD@CDQR^,@MBGDRSDQ"
             },
            {"plain": "over Newcastle.",
             "encrypted": "NUDQ^-DVB@RSKDl"
             },
            {"plain": "12466215376numbers{0!.,;:'^^%///(]=]{}\"'`",
             "encrypted": "oprttposqutMTLADQRZn_ljyxe==cmmmf<{<Z\\`e?"
             },
        ],
        [
            {"plain": "Mohamed Salah",
             "encrypted": "Ce^Wc[ZuIWbW^"
             },
            {"plain": "scored his 22nd",
             "encrypted": "iYeh[Zu^_iu((dZ"
             },
            {"plain": "League leaders Manchester",
             "encrypted": "B[W]k[ub[WZ[hiuCWdY^[ij[h"
             },
            {"plain": "over Newcastle.",
             "encrypted": "el[huD[mYWijb[$"
             },
            {"plain": "12466215376numbers{0!.,;:'^^%///(]=]{}\"'`",
             "encrypted": "'(*,,('+)-,dkcX[hiq&v$\"10|TTz%%%}S3Sqsw|V"
             },
        ]
    ]


if __name__ == '__main__':
    unittest.main()
