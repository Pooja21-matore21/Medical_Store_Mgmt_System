class Medicare:

    def __init__(self, mid, mediname, exp_date, price, quant):
        self.m_id = mid
        self.m_name = mediname
        # self.mfd_date = mfd_date
        self.expiry_date = exp_date
        self.price = price
        self.quantity = quant

    def __str__(self):
        data = str(self.m_id)+","+self.m_name+","+str(self.expiry_date) + \
            ","+str(self.price)+","+str(self.quantity)
        return data


class customerMedidata:

    def __init__(self, mid, quant):
        self.m_id = mid
        # self.m_name = mediname
        self.quantity = quant
        # self.total = total

    def __str__(self):
        data = str(self.m_id)+"," + \
            str(self.quantity)
        return data


class Bills:

    def __init__(self, mid, mediname, quantity, total):
        self.mid = mid
        self.mediname = mediname
        self.quant = quantity
        self.total = total

    def __str__(self):
        data = str(self.mid)+","+self.mediname+"," + \
            str(self.quant)+","+str(self.total)
        return data
