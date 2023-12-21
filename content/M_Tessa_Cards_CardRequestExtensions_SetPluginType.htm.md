# CardRequestExtensions.SetPluginType - метод
Устанавливает тип плагина при выполнении запроса к карточке из плагина
Chronos. Стандартные типы перечислены в
[CardPluginTypes](T_Tessa_Cards_CardPluginTypes.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetPluginType(
    	this CardInfoStorageObject request,
    	Guid? pluginType
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetPluginType ( 
    	request As CardInfoStorageObject,
    	pluginType As Guid?
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetPluginType(
    	CardInfoStorageObject^ request, 
    	Nullable<Guid> pluginType
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetPluginType : 
            request : CardInfoStorageObject * 
            pluginType : Nullable<Guid> -> unit 
#### Параметры
request [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Запрос к сервису карточек.
pluginType
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Тип плагина, из которого выполнен запрос, или null, если запрос выполнен не из плагина или из неизвестного плагина. 
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
