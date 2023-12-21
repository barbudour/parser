# CardRequestExtensions.GetKeepTaskDialog(CardResponseBase) - метод
Возвращает значение показывающее требуется ли оставить открытым окно диалога
или нет.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool GetKeepTaskDialog(
    	this CardResponseBase response
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetKeepTaskDialog ( 
    	response As CardResponseBase
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool GetKeepTaskDialog(
    	CardResponseBase^ response
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetKeepTaskDialog : 
            response : CardResponseBase -> bool 
#### Параметры
response [CardResponseBase](T_Tessa_Cards_CardResponseBase.htm)
    Ответ на запрос к сервису карточек.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение true, если окно диалога должно остаться открытым, иначе - false.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardResponseBase](T_Tessa_Cards_CardResponseBase.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[GetKeepTaskDialog -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_GetKeepTaskDialog.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
