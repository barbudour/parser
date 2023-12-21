# CardRequestExtensions.GetADFSAuthenticationResponse - метод
Возвращает сериализованную в XML информацию в виде строки, которая получена
при автоматическом создании сотрудника средствами ADFS, или null, если не
выполняется автоматическое создание сотрудника.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetADFSAuthenticationResponse(
    	this CardStoreRequest request
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetADFSAuthenticationResponse ( 
    	request As CardStoreRequest
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    static String^ GetADFSAuthenticationResponse(
    	CardStoreRequest^ request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetADFSAuthenticationResponse : 
            request : CardStoreRequest -> string 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на создание (первое сохранение) карточки сотрудника.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Сериализованная в XML информация в виде строки, которая получена при
автоматическом создании сотрудника средствами ADFS, или null, если не
выполняется автоматическое создание сотрудника.
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
