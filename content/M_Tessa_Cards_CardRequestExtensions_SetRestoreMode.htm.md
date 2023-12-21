# CardRequestExtensions.SetRestoreMode - метод
Устанавливает признак того, что при удалении удалённой карточки одновременно
выполняется восстановление карточки, которая была удалена.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetRestoreMode(
    	this CardDeleteRequest request,
    	bool restoreMode
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetRestoreMode ( 
    	request As CardDeleteRequest,
    	restoreMode As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetRestoreMode(
    	CardDeleteRequest^ request, 
    	bool restoreMode
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetRestoreMode : 
            request : CardDeleteRequest * 
            restoreMode : bool -> unit 
#### Параметры
request [CardDeleteRequest](T_Tessa_Cards_CardDeleteRequest.htm)
    Запрос на удаление удалённой карточки.
restoreMode [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что при удалении удалённой карточки одновременно выполняется восстановление карточки, которая была удалена. 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardDeleteRequest](T_Tessa_Cards_CardDeleteRequest.htm). При
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
