# CardRequestExtensions.SetWithoutBackupOnly - метод
Устанавливает признак того, что пользователем запрошено принудительное
удаление карточки без возможности восстановления.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetWithoutBackupOnly(
    	this CardDeleteRequest request,
    	bool withoutBackupOnly
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetWithoutBackupOnly ( 
    	request As CardDeleteRequest,
    	withoutBackupOnly As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetWithoutBackupOnly(
    	CardDeleteRequest^ request, 
    	bool withoutBackupOnly
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetWithoutBackupOnly : 
            request : CardDeleteRequest * 
            withoutBackupOnly : bool -> unit 
#### Параметры
request [CardDeleteRequest](T_Tessa_Cards_CardDeleteRequest.htm)
    Запрос на удаление карточки.
withoutBackupOnly
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что пользователем запрошено принудительное удаление карточки без возможности восстановления. 
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
