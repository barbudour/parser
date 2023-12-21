# ViewRowHelper - класс
Методы расширения для [ITessaViewResult](T_Tessa_Views_ITessaViewResult.htm)
##  __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ViewRowHelper
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class ViewRowHelper
C++ __Копировать
    [ExtensionAttribute]
    public ref class ViewRowHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type ViewRowHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ViewRowHelper
##  __Методы
[ConvertToDictionary](M_Tessa_Views_ViewRowHelper_ConvertToDictionary.htm)|
Пробразует результат выполнения запроса к представлению в список строк
карточки  
---|---  
[GetCardID](M_Tessa_Views_ViewRowHelper_GetCardID.htm)|  Возвращает
идентификатор карточки по заданному референсу.  
[GetCardIDAsInteger](M_Tessa_Views_ViewRowHelper_GetCardIDAsInteger.htm)|
Возвращает числовой идентификатор карточки по заданному референсу.  
[GetDisplayValue](M_Tessa_Views_ViewRowHelper_GetDisplayValue.htm)|
Возвращает строку, соответствующую отображаемому для карточки значению по
заданному референсу.  
[GetFirstStringColumnByPrefix](M_Tessa_Views_ViewRowHelper_GetFirstStringColumnByPrefix.htm)|
Возвращает имя первого строкового поля начинающегося с префикса  
[GetFirstStringValueByPrefix](M_Tessa_Views_ViewRowHelper_GetFirstStringValueByPrefix.htm)|
Возвращает значение первого строкового поля с имененм начинающимся с префикса  
[GetValueID](M_Tessa_Views_ViewRowHelper_GetValueID.htm)|  Возвращает значение
свойства по его префиксу. Возвращаемое значение формируется из префикса и ID
или RowID в зависимости от того что существует.  
[GetValuesByPrefix](M_Tessa_Views_ViewRowHelper_GetValuesByPrefix.htm)|
Возвращает список значений полей начинающихся с имени префикса  
[TryGetCardID](M_Tessa_Views_ViewRowHelper_TryGetCardID.htm)|  Возвращает
идентификатор карточки, полученный по значению из строки представления, или
null, если значение невозможно преобразовать к идентификатору.  
[TryGetCardIDAsInteger](M_Tessa_Views_ViewRowHelper_TryGetCardIDAsInteger.htm)|
Возвращает идентификатор карточки как числовое значение, полученное по
значению из строки представления, или null, если значение невозможно
преобразовать к числовому идентификатору.  
## __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
