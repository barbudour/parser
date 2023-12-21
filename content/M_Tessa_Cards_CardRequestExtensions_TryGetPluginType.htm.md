# CardRequestExtensions.TryGetPluginType - метод
Возвращает тип плагина, установленный при выполнении запроса к карточке из
плагина Chronos, или null, если запрос выполнен не из плагина или из
неизвестного плагина.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Guid? TryGetPluginType(
    	this CardInfoStorageObject request
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetPluginType ( 
    	request As CardInfoStorageObject
    ) As Guid?
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Nullable<Guid> TryGetPluginType(
    	CardInfoStorageObject^ request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetPluginType : 
            request : CardInfoStorageObject -> Nullable<Guid> 
#### Параметры
request [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Запрос к сервису карточек.
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>  
Тип плагина, из которого выполнен запрос, или null, если запрос выполнен не из
плагина или из неизвестного плагина.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
