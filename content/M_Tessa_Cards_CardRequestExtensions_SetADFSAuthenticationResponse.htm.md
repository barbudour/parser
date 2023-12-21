# CardRequestExtensions.SetADFSAuthenticationResponse - метод
Устанавливает сериализованную в XML информацию в виде строки, которая получена
при автоматическом создании сотрудника средствами ADFS, или null, если
информацию требуется удалить.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetADFSAuthenticationResponse(
    	this CardStoreRequest request,
    	string adfsAuthenticationResponse
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetADFSAuthenticationResponse ( 
    	request As CardStoreRequest,
    	adfsAuthenticationResponse As String
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetADFSAuthenticationResponse(
    	CardStoreRequest^ request, 
    	String^ adfsAuthenticationResponse
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetADFSAuthenticationResponse : 
            request : CardStoreRequest * 
            adfsAuthenticationResponse : string -> unit 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на создание (первое сохранение) карточки сотрудника.
adfsAuthenticationResponse
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Сериализованная в XML информация в виде строки, которая получена при автоматическом создании сотрудника средствами ADFS, или null, если информацию требуется удалить. 
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
