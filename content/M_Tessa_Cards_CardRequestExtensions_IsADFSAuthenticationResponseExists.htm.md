# CardRequestExtensions.IsADFSAuthenticationResponseExists - метод
Возвращает признак того, что в заданном запросе автоматически создаётся
сотрудник при входе в ADFS, т.е. при успешной авторизации по ADFS для
сотрудника, отсутствующего в Tessa, создаётся и заполняется карточка.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IsADFSAuthenticationResponseExists(
    	this CardStoreRequest request
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function IsADFSAuthenticationResponseExists ( 
    	request As CardStoreRequest
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool IsADFSAuthenticationResponseExists(
    	CardStoreRequest^ request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member IsADFSAuthenticationResponseExists : 
            request : CardStoreRequest -> bool 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на создание (первое сохранение) карточки сотрудника.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если в заданном запросе создаётся сотрудник средствами ADFS; false в
противном случае.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm). При
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
