# CardRequestExtensions.SetKeepTaskDialog(CardResponseBase, Boolean) - метод
Устанавливает в [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm) объекта
[CardResponseBase](T_Tessa_Cards_CardResponseBase.htm) флаг показывающий
требуется ли оставить открытым окно диалога или нет.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetKeepTaskDialog(
    	this CardResponseBase response,
    	bool value = true
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetKeepTaskDialog ( 
    	response As CardResponseBase,
    	Optional value As Boolean = true
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetKeepTaskDialog(
    	CardResponseBase^ response, 
    	bool value = true
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetKeepTaskDialog : 
            response : CardResponseBase * 
            ?value : bool 
    (* Defaults:
            let _value = defaultArg value true
    *)
    -> unit 
#### Параметры
response [CardResponseBase](T_Tessa_Cards_CardResponseBase.htm)
    Ответ на запрос к сервису карточек в котором должен быть установлен флаг.
value [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
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
[SetKeepTaskDialog -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_SetKeepTaskDialog.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
