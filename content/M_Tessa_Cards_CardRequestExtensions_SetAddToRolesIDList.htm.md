# CardRequestExtensions.SetAddToRolesIDList - метод
Устанавливает список идентификаторов ролей, в которые должен быть добавлен
создаваемый сотрудник в запросе на создание (первое сохранение) карточки
сотрудника [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm). Если при
включении сотрудника в одну из ролей возникнет ошибка, то она будет добавлена
как предупреждение, и включение в другие роли, а также сохранение завершатся
успешно.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetAddToRolesIDList(
    	this CardStoreRequest request,
    	ICollection<Guid> roleIDList
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetAddToRolesIDList ( 
    	request As CardStoreRequest,
    	roleIDList As ICollection(Of Guid)
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetAddToRolesIDList(
    	CardStoreRequest^ request, 
    	ICollection<Guid>^ roleIDList
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetAddToRolesIDList : 
            request : CardStoreRequest * 
            roleIDList : ICollection<Guid> -> unit 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на создание (первое сохранение) карточки сотрудника.
roleIDList
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Список идентификаторов ролей, в которые должен быть добавлен создаваемый сотрудник. Значение null определяет, что список идентификаторов должен быть удалён. 
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
