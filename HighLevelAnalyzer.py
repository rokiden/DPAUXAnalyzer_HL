# High Level Analyzer
# For more information and documentation, please go to https://support.saleae.com/extensions/high-level-analyzer-extensions

from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame, StringSetting, NumberSetting, ChoicesSetting

dpcd_regs = {
    0x00000: 'REV',
    0x00001: 'MAX_LINK_RATE',
    0x00002: 'MAX_LANE_COUNT',
    0x00003: 'MAX_DOWNSPREAD',
    0x00004: 'NORP_PWR_V_CAP',
    0x00005: 'DOWNSP_PRESENT',
    0x00006: 'ML_CH_CODING_CAP',
    0x00007: 'DOWNSP_COUNT_MSA_OUI',
    0x00008: 'RX_PORT0_CAP_0',
    0x00009: 'RX_PORT0_CAP_1',
    0x0000A: 'RX_PORT1_CAP_0',
    0x0000B: 'RX_PORT1_CAP_1',
    0x0000C: 'I2C_SPEED_CTL_CAP',
    0x0000D: 'EDP_CFG_CAP',
    0x0000E: 'TRAIN_AUX_RD_INTERVAL',
    0x0000F: 'ADAPTER_CAP',
    0x00021: 'MSTM_CAP',
    0x00022: 'NUM_AUDIO_EPS',
    0x00023: 'AV_GRANULARITY',
    0x00024: 'AUD_DEC_LAT_7_0',
    0x00025: 'AUD_DEC_LAT_15_8',
    0x00026: 'AUD_PP_LAT_7_0',
    0x00027: 'AUD_PP_LAT_15_8',
    0x00028: 'VID_INTER_LAT',
    0x00029: 'VID_PROG_LAT',
    0x0002A: 'REP_LAT',
    0x0002B: 'AUD_DEL_INS_7_0',
    0x0002C: 'AUD_DEL_INS_15_8',
    0x0002D: 'AUD_DEL_INS_23_16',
    0x00030: 'GUID',
    0x00054: 'RX_GTC_VALUE_7_0',
    0x00055: 'RX_GTC_VALUE_15_8',
    0x00056: 'RX_GTC_VALUE_23_16',
    0x00057: 'RX_GTC_VALUE_31_24',
    0x00058: 'RX_GTC_MSTR_REQ',
    0x00059: 'RX_GTC_FREQ_LOCK_DONE',
    0x00080: 'DOWNSP_0_CAP',
    0x00081: 'DOWNSP_1_CAP',
    0x00082: 'DOWNSP_2_CAP',
    0x00083: 'DOWNSP_3_CAP',
    # 0x00080: 'DOWNSP_0_DET_CAP',
    0x00084: 'DOWNSP_1_DET_CAP',
    0x00088: 'DOWNSP_2_DET_CAP',
    0x0008C: 'DOWNSP_3_DET_CAP',

    0x00020: 'FAUX_DEPRECATED',
    0x00060: 'DSC_SUPPORT',

    0x00090: 'FEC_CAPABILITY',

    0x00070: 'Panel_Self_Refresh',

    0x000B0: 'PANEL_REPLAY_CAP',

    0x00300: 'SRC_IEEE_OUI',
    0x00400: 'SNK_IEEE_OUI',
    0xE0000: 'TUN_IEEE_OUI',
    0xE000D: 'TUN_IEEE_OUI_SPECIFIC',

    0x00100: 'LINK_BW_SET',
    0x00101: 'LANE_COUNT_SET',
    0x00102: 'TP_SET',
    0x00103: 'TRAINING_LANE0_SET',
    0x00104: 'TRAINING_LANE1_SET',
    0x00105: 'TRAINING_LANE2_SET',
    0x00106: 'TRAINING_LANE3_SET',
    0x00107: 'DOWNSPREAD_CTRL',
    0x00108: 'ML_CH_CODING_SET',
    0x00109: 'I2C_SPEED_CTL_SET',
    0x0010A: 'EDP_CFG_SET',
    0x0010B: 'LINK_QUAL_LANE0_SET',
    0x0010C: 'LINK_QUAL_LANE1_SET',
    0x0010D: 'LINK_QUAL_LANE2_SET',
    0x0010E: 'LINK_QUAL_LANE3_SET',
    0x0010F: 'TRAINING_LANE0_1_SET2',
    0x00110: 'TRAINING_LANE2_3_SET2',
    0x00111: 'MSTM_CTRL',
    0x00112: 'AUDIO_DELAY_7_0',
    0x00113: 'AUDIO_DELAY_15_8',
    0x00114: 'AUDIO_DELAY_23_6',
    0x00118: 'UPSTREAM_DEVICE_DP_PWR_NEED',
    0x00120: 'FEC_CONFIGURATION',
    0x00121: 'FAUX_FORWARD_CH_DRIVE_SET',
    0x00122: 'BACK_CH_STATUS',
    0x00123: 'FAUX_BACK_CH_SYMBOL_ERROR_COUNT',
    0x00125: 'FAUX_BACK_CH_TRAINING_PATTERN_TIME',
    0x00154: 'TX_GTC_VALUE_7_0',
    0x00155: 'TX_GTC_VALUE_15_8',
    0x00156: 'TX_GTC_VALUE_23_16',
    0x00157: 'TX_GTC_VALUE_31_24',
    0x00158: 'RX_GTC_VALUE_PHASE_SKEW_EN',
    0x00159: 'TX_GTC_FREQ_LOCK_DONE',
    0x00160: 'DSC_ENABLE',
    0x001A0: 'ADAPTER_CTRL',
    0x001A1: 'BRANCH_DEVICE_CTRL',
    0x001C0: 'PLD_ALLOCATE_SET',
    0x001C1: 'PLD_ALLOCATE_START_TIME_SLOT',
    0x001C2: 'PLD_ALLOCATE_TIME_SLOT_COUNT',

    0x00200: 'SINK_COUNT',
    0x00201: 'DEVICE_SERVICE_IRQ',
    0x00202: 'STATUS_LANE_0_1',
    0x00203: 'STATUS_LANE_2_3',
    0x00204: 'LANE_ALIGN_STATUS_UPDATED',
    0x00205: 'SINK_STATUS',
    0x00206: 'ADJ_REQ_LANE_0_1',
    0x00207: 'ADJ_REQ_LANE_2_3',
    0x00208: 'TRAINING_SCORE_LANE_0',
    0x00209: 'TRAINING_SCORE_LANE_1',
    0x0020A: 'TRAINING_SCORE_LANE_2',
    0x0020B: 'TRAINING_SCORE_LANE_3',
    0x0020C: 'ADJ_REQ_PC2',
    0x0020D: 'FAUX_FORWARD_CH_SYMBOL_ERROR_COUNT',
    0x00210: 'SYMBOL_ERROR_COUNT_LANE_0',
    0x00212: 'SYMBOL_ERROR_COUNT_LANE_1',
    0x00214: 'SYMBOL_ERROR_COUNT_LANE_2',
    0x00216: 'SYMBOL_ERROR_COUNT_LANE_3',
    0x00280: 'FAUX_FORWARD_CH_STATUS',
    0x00281: 'FAUX_BACK_CH_DRIVE_SET',
    0x00282: 'FAUX_BACK_CH_SYM_ERR_COUNT_CTRL',
    0x002C0: 'PLD_TABLE_UPDATE_STATUS',

    0x00600: 'SET_POWER_DP_PWR_VOLTAGE',

    0x01000: 'SB_DOWN_REQ',
    0x01200: 'SB_UP_REP',
    0x01400: 'SB_DOWN_REP',
    0x01600: 'SB_UP_REQ',

    0x02002: 'SINK_COUNT_ESI',
    0x02003: 'SINK_DEV_SERVICE_IRQ_VCT_ESI0',
    0x02004: 'SINK_DEV_SERVICE_IRQ_VCT_ESI1',
    0x02005: 'SINK_LINK_SERVICE_IRQ_VCT_ESI0',
    0x0200C: 'SINK_LANE0_1_STATUS',
    0x0200D: 'SINK_LANE2_3_STATUS',
    0x0200E: 'SINK_ALIGN_STATUS_UPDATED_ESI',
    0x0200F: 'SINK_STATUS_ESI',
    0x02200: 'EXT_DPCD_REV',
    0x02201: 'EXT_DPCD_MAX_LINK_RATE',
    0x02210: 'FEATURE_ENUMERATION_LIST',
    0x02211: 'EXT_DPRX_SLP_WAKE_TIMEOUT_REQ',

    0xF0000: 'LTTPR_FIELD_DATA_STRUCT_REV',
    0xF0001: 'LTTPR_MAX_LINK_RATE',
    0xF0002: 'LTTPR_PHY_REPEATER_CNT',
    0xF0003: 'LTTPR_PHY_REPEATER_MODE',
    0xF0004: 'LTTPR_MAX_LANE_COUNT',
    0xF0005: 'LTTPR_EXT_WAIT_TIMEOUT',

    0xF0010: 'LTTPR1_TRAINING_PATTERN_SET',
    0xF0011: 'LTTPR1_TRAINING_LANE0_SET',
    0xF0012: 'LTTPR1_TRAINING_LANE1_SET',
    0xF0013: 'LTTPR1_TRAINING_LANE2_SET',
    0xF0014: 'LTTPR1_TRAINING_LANE3_SET',
    0xF0020: 'LTTPR1_TRAINING_AUX_RD_INTERVAL',
    0xF0021: 'LTTPR1_TRANSMITTER_CAP_PHY',
    0xF0030: 'LTTPR1_LANE0_1_STATUS',
    0xF0032: 'LTTPR1_LANE_ALIGN_STATUS_UPDATED_PHY',
    0xF0033: 'LTTPR1_ADJUST_REQUEST_LANE0_1',

    0xF0294: 'FEC_CAP_PHY_RPT1',

    0x68000: 'HDCP1_BKSV',
    0x68005: 'HDCP1_R0',
    0x68007: 'HDCP1_AKSV',
    0x6800C: 'HDCP1_AN',
    0x68014: 'HDCP1_V',
    0x68028: 'HDCP1_BCAPS',
    0x68029: 'HDCP1_BSTATUS',
    0x6802A: 'HDCP1_BINFO',
    0x6802C: 'HDCP1_KSVFIFO',
    0x6803B: 'HDCP1_AINFO',
    0x6803C: 'HDCP1_RSVD',

    0x69000: 'HDCP2_RTX',
    0x69008: 'HDCP2_TXCAPS',
    0x6900B: 'HDCP2_CERTRX',
    0x69215: 'HDCP2_RRX',
    0x6921D: 'HDCP2_RXCAPS',
    0x69220: 'HDCP2_EKPUB_KM',
    0x692A0: 'HDCP2_EKH_KM_WR',
    0x692B0: 'HDCP2_M',
    0x692C0: 'HDCP2_HPRIME',
    0x692E0: 'HDCP2_EKH_KM_RD',
    0x692F0: 'HDCP2_RN',
    0x692F8: 'HDCP2_LPRIME',
    0x69318: 'HDCP2_EDKEY_KS',
    0x69328: 'HDCP2_RIV',
    0x69330: 'HDCP2_RXINFO',
    0x69332: 'HDCP2_SEQ_NUM_V',
    0x69335: 'HDCP2_VPRIME',
    0x69345: 'HDCP2_RECEIVER_ID_LIST',
    0x693E0: 'HDCP2_V',
    0x693F0: 'HDCP2_SEQ_NUM_M',
    0x693F3: 'HDCP2_K',
    0x693F5: 'HDCP2_STREAMID_TYPE',
    0x69473: 'HDCP2_MPRIME',
    0x69493: 'HDCP2_RXSTATUS',
    0x69494: 'HDCP2_TYPE',


}


# High level analyzers must subclass the HighLevelAnalyzer class.
class Hla(HighLevelAnalyzer):
    # List of settings that a user can set for this High Level Analyzer.
    # my_string_setting = StringSetting()
    # my_number_setting = NumberSetting(min_value=0, max_value=100)
    # my_choices_setting = ChoicesSetting(choices=('A', 'B'))

    # An optional list of types this analyzer produces, providing a way to customize the way frames are displayed in Logic 2.
    result_types = {
        'ERR': {'format': '{{type}}: {{data.msg}}'},
        'REQ': {'format': '{{type}} {{data.subtype}} {{data.addr}} {{data.reg}} {{data.len}} {{data.data}}'},
        'RPL': {'format': '{{type}} {{data.subtype}} {{data.len}} {{data.data}}'},
    }

    def __init__(self):
        '''
        Initialize HLA.

        Settings can be accessed using the same name used above.
        '''

        # print("Settings:", self.my_string_setting,
        #       self.my_number_setting, self.my_choices_setting)

        self.next = ('SYNC',)
        self.frames = []
        self.wait_reply = False
        self.prev_ftype = ''
        self.prev_fdata = {}
        self.prev_data = {}

    def parse_transaction(self, words):
        data = {'subtype': '',
                'len': None,
                'data': None,
                'addr': None, }
        comm = words[0] >> 4
        if self.wait_reply:
            self.wait_reply = False
            assert words[0] & 0b1111 == 0, 'invalid RPL COMM'
            ftype = 'RPL'

            naux = comm & 0b11
            iaux = comm >> 2
            caux = naux | iaux

            if caux == 0:
                data['subtype'] = 'ACK'
            else:
                if caux & 1:
                    data['subtype'] = 'NACK'
                if caux & 2:
                    data['subtype'] += (' ' if data['subtype'] else '') + 'DEFER'

            data['data'] = words[1:]
            data['len'] = len(data['data'])
        else:
            self.wait_reply = True
            assert len(words) >= 4, 'REQ too short'  # com|addr + len
            ftype = 'REQ'

            if comm >> 3:  # DP
                req_type = comm & 0b111
                assert req_type < 2, 'invalid REQ TYPE'
                data['subtype'] = 'N' + ('R' if req_type else 'W')
            else:  # I2C
                mot = (comm >> 2) & 1
                req_type = comm & 0b11
                assert req_type < 3, 'invalid REQ TYPE'
                data['subtype'] = 'I' + ('WRS'[req_type]) + ('M' if mot else '')

            data['addr'] = ((words[0] & 0b1111) << 16) | (words[1] << 8) | words[2]
            data['len'] = words[3] + 1
            data['data'] = words[4:]

        fdata = {'subtype': data['subtype']}
        if data['addr'] is not None:
            fdata['addr'] = f"{data['addr']:05X}"
        if data['addr'] in dpcd_regs:
            fdata['reg'] = dpcd_regs[data['addr']]
        if data['data'] is not None:
            fdata['data'] = ''.join(map(lambda d: f'{d:02X}', data['data']))
        if data['len'] is not None:
            fdata['len'] = str(data['len'])

        if ftype == 'RPL' and self.prev_ftype == 'REQ':
            if self.prev_fdata['subtype'] == 'NR':
                print(
                    f"{self.prev_fdata['subtype']} {self.prev_fdata['addr']} {self.prev_fdata.get('reg', '')} {self.prev_fdata['len']} -> {fdata['subtype']} {fdata['len']} {fdata['data']}")
            elif self.prev_fdata['subtype'] == 'NW':
                print(
                    f"{self.prev_fdata['subtype']} {self.prev_fdata['addr']} {self.prev_fdata.get('reg', '')} {self.prev_fdata['len']} {self.prev_fdata['data']} -> {fdata['subtype']}")
            elif self.prev_fdata['subtype'].startswith('IW'):
                print(
                    f"{self.prev_fdata['subtype']} {self.prev_fdata['addr']} {self.prev_fdata['len']} {self.prev_fdata['data']} -> {fdata['subtype']}")
            elif self.prev_fdata['subtype'].startswith('IR'):
                print(
                    f"{self.prev_fdata['subtype']} {self.prev_fdata['addr']} {self.prev_fdata['len']} -> {fdata['subtype']} {fdata['len']} {fdata['data']}")
            else:
                print('skip')

        self.prev_data = data
        self.prev_ftype = ftype
        self.prev_fdata = fdata
        return ftype, fdata

    def decode(self, frame: AnalyzerFrame):
        '''
        Process a frame from the input analyzer, and optionally return a single `AnalyzerFrame` or a list of `AnalyzerFrame`s.

        The type and data values in `frame` will depend on the input analyzer.
        '''

        # print('decode', frame.type, frame.data)

        if frame.type not in self.next:
            msg = f"{frame.type} instead of {' or '.join(self.next)}"
            f = AnalyzerFrame('ERR', frame.start_time, frame.end_time, {'msg': msg})
            print("ERR:", msg)
            self.next = ('SYNC',)
            self.frames.clear()
            return f
        else:
            self.frames.append(frame)
            if frame.type == 'SYNC':
                self.next = ('START',)
            elif frame.type == 'START':
                self.next = ('DATA',)
            elif frame.type == 'DATA':
                self.next = ('DATA', 'STOP',)
            elif frame.type == 'STOP':
                self.next = ('SYNC',)
                # print('->'.join(map(lambda f: f.type, self.frames)))
                datas = [f.data['value'][0] for f in self.frames if f.type == 'DATA']
                # print(datas)
                try:
                    ftype, fdata = self.parse_transaction(datas)
                except AssertionError as e:
                    msg = str(e) or 'assert'
                    ftype, fdata = 'ERR', {'msg': msg}
                    print("ERR:", msg)

                f = AnalyzerFrame(ftype, self.frames[0].start_time, self.frames[-1].end_time, fdata)
                self.frames.clear()
                return f
