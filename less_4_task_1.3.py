"""Сформировать из введенного числа обратное по порядку входящих в него цифр
 и вывести на экран. Например, если введено число 3486, надо вывести 6843."""
import timeit
import cProfile


def digit_reverse(digit):  # Решение через строчный ввод
    digit = str(digit)
    result = list(digit)
    for i in range(len(digit) // 2):
        tmp = result[i]
        result[i] = result[len(digit) - i - 1]
        result[len(digit) - i - 1] = tmp
    return ''.join(result)


print(timeit.timeit('digit_reverse(12)', number=1000, globals=globals()))  # 0.0007469
print(timeit.timeit('digit_reverse(121)', number=1000, globals=globals()))  # 0.0006717000000000008
print(timeit.timeit('digit_reverse(1221)', number=1000, globals=globals()))  # 0.0008022999999999988
print(timeit.timeit('digit_reverse(12321)', number=1000, globals=globals()))  # 0.000815299999999998
print(timeit.timeit('digit_reverse(123321)', number=1000, globals=globals()))  # 0.0009460999999999983
print(timeit.timeit('digit_reverse(12345674312345342123)', number=1000, globals=globals()))  # 0.0019168999999999992
print(timeit.timeit('digit_reverse(123456743123497069867979065342123)', number=1000,
                    globals=globals()))  # 0.002854200000000001
print(timeit.timeit('digit_reverse(12345674312349706986743536634634466442123)', number=1000,
                    globals=globals()))  # 0.0033264
print(timeit.timeit('digit_reverse(12345674312349706986734453454353453453453455345343542123)', number=1000,
                    globals=globals()))  # 0.004361400000000001
print(timeit.timeit('digit_reverse(12345674312349706986734453454353453453453455345343542123565645656456644565656656)'
                    , number=1000, globals=globals()))  # 0.006210199999999999

cProfile.run(
    'digit_reverse(1231243547687978890785674323293523952368562836582357836257325723568787253787235563878287542354364565'
    '645635342423424345645645646423423425367987980890667979797898797897979756757586970808908908908908989090004242342344'
    '234234324242342424234242342467678679789898908876856745456464534523423424235345687978890890890890898979798797056464'
    '456457567563452345345345645645654756756757453432453453453464565756756756753464575686778898098908908908909524312441'
    '436456768678785674534245345456567678978989899089009909090086796563424243545767867979889789797090999990908676766834'
    '234235464657564523423656788987989678675645634546566876778978978978967856756453453453453453454565675676786788678643'
    '234245456765654322435467567678678678678567456463435354565675686786786786585674563453342423434656897897896797896793'
    '342345345464566575754746345234234123131231313423534534565676786787867878797897899000998787667452342547567876789845'
    '234234346576867878678567456345234234234345457567567456345235423543456475687897809967856745234242354756677876786812'
    '324235345456456567678678797897896756454342545767878987897685645345345346567867978987967856745634564576797898908900'
    '232456789654345678908765432456789087654324567898765434567890876543456789098765434567890876546789098765467897658789'
    '211434545767878967857452342353677586797967856354234235455686797897087563523234352311111233245454556677687879978934'
    '243656767878674635536577898090879563442342344575668708908989089078574534234342454456586897808908908908908908978676'
    '885488544395934204082942374238423747263424235178234923472984372934723957349573295734954365458935739475934957394595'
    '354436567567566786785645434234243455568678788908996745635234323534645656689878908979678567453453423424234242325345'
    '234354465756756745634523423423434545656678679789789878908967746354213423434645745768678789678675645345342342343432'
    '132122434546546756786786786775463453423412322345456456568678679878967967867856756453423423534654756756867867878788'
    '234234345456456456345234234243454575867867856745645234234123234354575686797808706785674563452342342342342342343433'
    '435456567678797896746345235354429427948623847238423897293742397529579832759238529835629835928356293859283562938592'
    '242343454565756875634534242434564575686797897896746345345234243454565475686786796796785674543423423534654767989988'
    '234234534645567797898089785674635232323432344565756867896797899789870890890898768756745645646456756768787989898998'
    '123235346547678675463423464424523454744234375674534534657678456353423445575675668787887978989879789789565657567567'
    '345634)')
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#      1    0.000    0.000    0.001    0.001 less_4_task_1.3.py:7(digit_reverse)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#   2501    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}


# В данном решении задачи использовалась замена вводящегося числа в строку, и переворот этой строки классическим методом
# Оценка задачи со стороны асимптотики: асимптотика линейная