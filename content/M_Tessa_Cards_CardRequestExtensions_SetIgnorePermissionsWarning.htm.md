# CardRequestExtensions.SetIgnorePermissionsWarning - метод
Устанавливает признак того, что при обработке карточки могут быть не указаны
токены безопасности, поэтому не следует показывать соответствующее
предупреждение.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetIgnorePermissionsWarning(
    	this CardInfoStorageObject request,
    	bool ignorePermissionsWarning = true
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetIgnorePermissionsWarning ( 
    	request As CardInfoStorageObject,
    	Optional ignorePermissionsWarning As Boolean = true
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetIgnorePermissionsWarning(
    	CardInfoStorageObject^ request, 
    	bool ignorePermissionsWarning = true
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetIgnorePermissionsWarning : 
            request : CardInfoStorageObject * 
            ?ignorePermissionsWarning : bool 
    (* Defaults:
            let _ignorePermissionsWarning = defaultArg ignorePermissionsWarning true
    *)
    -> unit 
#### Параметры
request [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Запрос к сервису карточек.
ignorePermissionsWarning
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что при сохранении карточки могут быть не указаны токены безопасности, поэтому не следует показывать соответствующее предупреждение. 
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
