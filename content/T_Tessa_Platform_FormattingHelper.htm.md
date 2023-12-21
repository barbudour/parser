# FormattingHelper - класс
Вспомогательные методы для форматирования данных в читаемом для пользователя
виде.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class FormattingHelper
VB __Копировать
     Public NotInheritable Class FormattingHelper
C++ __Копировать
     public ref class FormattingHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type FormattingHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FormattingHelper
##  __Методы
[ExtractPlainTextFromHtml](M_Tessa_Platform_FormattingHelper_ExtractPlainTextFromHtml.htm)|
Извлекает отображаемый текст из HTML-сообщения. Если передано значение не
null, то возвращается также не null.  
---|---  
[Format](M_Tessa_Platform_FormattingHelper_Format.htm)|  Форматирует значение
для вывода в читаемом для пользователя виде.  
[FormatDate(DateTime,
Boolean)](M_Tessa_Platform_FormattingHelper_FormatDate.htm)|  Форматирует дату
без времени для вывода в читаемом для пользователя виде.  
[FormatDate(Nullable<DateTime>,
Boolean)](M_Tessa_Platform_FormattingHelper_FormatDate_1.htm)|  Форматирует
дату без времени для вывода в читаемом для пользователя виде. Строка для
неизвестного времени отображается локализованной для текущего выбранного
языка.  
[FormatDateDiff](M_Tessa_Platform_FormattingHelper_FormatDateDiff.htm)|
Форматирует строку с временем, оставшимся до некоторого момента, по заданному
числу квантов. При этом используются единицы измерения, удобные для восприятия
человеку (часы, дни и др.)  
[FormatDateTime(DateTime,
Boolean)](M_Tessa_Platform_FormattingHelper_FormatDateTime.htm)|  Форматирует
дату и время для вывода в читаемом для пользователя виде.  
[FormatDateTime(Nullable<DateTime>,
Boolean)](M_Tessa_Platform_FormattingHelper_FormatDateTime_1.htm)|
Форматирует дату и время для вывода в читаемом для пользователя виде. Строка
для неизвестного времени отображается локализованной для текущего выбранного
языка.  
[FormatDateTimeWithoutSeconds(DateTime,
Boolean)](M_Tessa_Platform_FormattingHelper_FormatDateTimeWithoutSeconds.htm)|
Форматирует дату и время без указания секунд для вывода в читаемом для
пользователя виде.  
[FormatDateTimeWithoutSeconds(Nullable<DateTime>,
Boolean)](M_Tessa_Platform_FormattingHelper_FormatDateTimeWithoutSeconds_1.htm)|
Форматирует дату и время без указания секунд для вывода в читаемом для
пользователя виде. Строка для неизвестного времени отображается локализованной
для текущего выбранного языка.  
[FormatDecimal](M_Tessa_Platform_FormattingHelper_FormatDecimal.htm)|
Выполняет форматирование денежной суммы
[Decimal](https://learn.microsoft.com/dotnet/api/system.decimal) с
использованием заданной строки форматирования, которую рекомендуется получить
посредством метода
[GetDecimalFormatString(Int32)](M_Tessa_Platform_FormattingHelper_GetDecimalFormatString.htm).  
[FormatDoubleAsDecimal(Double,
Int32)](M_Tessa_Platform_FormattingHelper_FormatDoubleAsDecimal.htm)|
Форматирует вещественное число value в десятичном виде 123.45 с количеством
цифр после запятой, указанном в maxDigitsAfterDecimalPoint. Удаляет
завершающие нули после запятой, а также саму запятую, если число целое.
Форматирование выполняется в инвариантной культуре
[InvariantCulture](https://learn.microsoft.com/dotnet/api/system.globalization.cultureinfo.invariantculture#system-
globalization-cultureinfo-invariantculture).  
[FormatDoubleAsDecimal(Double, Int32,
CultureInfo)](M_Tessa_Platform_FormattingHelper_FormatDoubleAsDecimal_1.htm)|
Форматирует вещественное число value в десятичном виде 123.45 с количеством
цифр после запятой, указанном в maxDigitsAfterDecimalPoint. Удаляет
завершающие нули после запятой, а также саму запятую, если число целое.  
[FormatNullable(String)](M_Tessa_Platform_FormattingHelper_FormatNullable.htm)|
Возвращает исходную строку, если она не равна значению null, иначе возвращает
значение [NullText](F_Tessa_Platform_FormattingHelper_NullText.htm).  
[FormatNullable<T>(Nullable<T>)](M_Tessa_Platform_FormattingHelper_FormatNullable__1.htm)|
Возвращает строковое представление объекта, если он задан, иначе возвращает
значение [NullText](F_Tessa_Platform_FormattingHelper_NullText.htm).  
[FormatNullable<T>(Nullable<T>, Func<T,
String>)](M_Tessa_Platform_FormattingHelper_FormatNullable__1_1.htm)|
Возвращает строковое представление объекта, если он задан, иначе возвращает
значение [NullText](F_Tessa_Platform_FormattingHelper_NullText.htm).  
[FormatNullable<T>(Nullable<T>, String,
IFormatProvider)](M_Tessa_Platform_FormattingHelper_FormatNullable__1_2.htm)|
Возвращает строковое представление объекта, если он задан, иначе возвращает
значение [NullText](F_Tessa_Platform_FormattingHelper_NullText.htm).  
[FormatSessionDateTime](M_Tessa_Platform_FormattingHelper_FormatSessionDateTime.htm)|
Форматирует дату и время для вывода в читаемом для пользователя виде.  
[FormatSize(Int64, Int64)](M_Tessa_Platform_FormattingHelper_FormatSize.htm)|
Форматирует размер, заданный в байтах, в строку, в которой указан размер в
заданной единице измерения.  
[FormatSize(Int64,
SizeUnit)](M_Tessa_Platform_FormattingHelper_FormatSize_1.htm)|  Форматирует
размер, заданный в байтах, в строку, в которой указан размер в заданной
единице измерения.  
[FormatTime(Nullable<TimeSpan>)](M_Tessa_Platform_FormattingHelper_FormatTime_2.htm)|
Форматирует время, заданное объектом
[TimeSpan](https://learn.microsoft.com/dotnet/api/system.timespan), таким
образом, что оно содержит часы, минуты и секунды.  
[FormatTime(TimeSpan)](M_Tessa_Platform_FormattingHelper_FormatTime_3.htm)|
Форматирует время, заданное объектом
[TimeSpan](https://learn.microsoft.com/dotnet/api/system.timespan), таким
образом, что оно содержит часы, минуты и секунды.  
[FormatTime(DateTime,
Boolean)](M_Tessa_Platform_FormattingHelper_FormatTime.htm)|  Форматирует
время без даты для вывода в читаемом для пользователя виде.  
[FormatTime(Nullable<DateTime>,
Boolean)](M_Tessa_Platform_FormattingHelper_FormatTime_1.htm)|  Форматирует
время без даты для вывода в читаемом для пользователя виде. Строка для
неизвестного времени отображается локализованной для текущего выбранного
языка.  
[FormatTimeWithoutSeconds(Nullable<TimeSpan>)](M_Tessa_Platform_FormattingHelper_FormatTimeWithoutSeconds.htm)|
Форматирует время, заданное объектом
[TimeSpan](https://learn.microsoft.com/dotnet/api/system.timespan), таким
образом, что оно содержит часы и минуты без секунд.  
[FormatTimeWithoutSeconds(TimeSpan)](M_Tessa_Platform_FormattingHelper_FormatTimeWithoutSeconds_1.htm)|
Форматирует время, заданное объектом
[TimeSpan](https://learn.microsoft.com/dotnet/api/system.timespan), таким
образом, что оно содержит часы и минуты без секунд.  
[FormatToString(Object,
Boolean)](M_Tessa_Platform_FormattingHelper_FormatToString.htm)|  Форматирует
значение в строку для вывода в читаемом для пользователя виде. Возвращённое
значение может быть равно null.  
[FormatToString(Object, String,
Boolean)](M_Tessa_Platform_FormattingHelper_FormatToString_1.htm)|
Форматирует значение в строку для вывода в читаемом для пользователя виде.
Возвращённое значение может быть равно null.  
[FormatUnit](M_Tessa_Platform_FormattingHelper_FormatUnit.htm)|  Возвращает
сокращённое строковое представление для заданной единицы измерения размера. Не
возвращает пробел в начале строки.  
[FormatUtcOffset](M_Tessa_Platform_FormattingHelper_FormatUtcOffset.htm)|
Выполняет форматирование смещения относительно UTC в виде "+3:00" или
"-11:30". Нулевое смещение выводится как "+0:00".  
[GetDecimalFormatString](M_Tessa_Platform_FormattingHelper_GetDecimalFormatString.htm)|
Возвращает строку форматирования для денежных сумм
[Decimal](https://learn.microsoft.com/dotnet/api/system.decimal) с заданным
количеством знаков после запятой. При этом учитываются разделители групп
символов. Строку рекомендуется использовать в методе [FormatDecimal(Decimal,
String)](M_Tessa_Platform_FormattingHelper_FormatDecimal.htm).  
[GetUnitString](M_Tessa_Platform_FormattingHelper_GetUnitString.htm)|
Возвращает словоформу, подходящую к количеству некоторых единиц units.  
[ParseDateTime](M_Tessa_Platform_FormattingHelper_ParseDateTime.htm)|
Выполняет парсинг даты/времени, независимо от текущей культуры в потоке и с
учётом того, что преобразование даты в строку выполнялось посредством методов
форматирования FormattingHelper.  
[ParseSize(String, Int64)](M_Tessa_Platform_FormattingHelper_ParseSize.htm)|
Преобразует строку, содержащую отформатированный размер в заданной единице
измерения, в значение размера в байтах.  
[ParseSize(String,
SizeUnit)](M_Tessa_Platform_FormattingHelper_ParseSize_1.htm)|  Преобразует
строку, содержащую отформатированный размер в заданной единице измерения, в
значение размера в байтах.  
## __Поля
[EmailRegex](F_Tessa_Platform_FormattingHelper_EmailRegex.htm)|  Регулярное
выражение для проверки строки на то, что она является корректным e-mail.
Доменное имя первого уровня должно содержать хотя бы один символ, но может
содержать и больше трёх символов, например: user@domain-name.local.  
---|---  
[EmptyText](F_Tessa_Platform_FormattingHelper_EmptyText.htm)|  Строка,
отображаемая, если в коллекции не содержится элементов.  
[NullText](F_Tessa_Platform_FormattingHelper_NullText.htm)|  Строка,
отображаемая вместо значения null в методах
[FormatNullable(String)](M_Tessa_Platform_FormattingHelper_FormatNullable.htm).  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
