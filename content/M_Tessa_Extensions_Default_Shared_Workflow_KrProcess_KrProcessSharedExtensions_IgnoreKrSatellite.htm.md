# KrProcessSharedExtensions.IgnoreKrSatellite - метод
Устанавливает значение, показывающее, что при загрузке карточки не надо
загружать и обрабатывать информацию содержащуюся в основном сателлите
([KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm))
карточки.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void IgnoreKrSatellite(
    	this CardInfoStorageObject request,
    	bool value = true
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub IgnoreKrSatellite ( 
    	request As CardInfoStorageObject,
    	Optional value As Boolean = true
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void IgnoreKrSatellite(
    	CardInfoStorageObject^ request, 
    	bool value = true
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member IgnoreKrSatellite : 
            request : CardInfoStorageObject * 
            ?value : bool 
    (* Defaults:
            let _value = defaultArg value true
    *)
    -> unit 
#### Параметры
request [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Хранилище в котором устанавливается флаг.
value [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Значение true, если при загрузке карточки не надо загружать и обрабатывать информацию содержащуюся в основном сателлите ([KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm)) карточки, иначе - false.
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
[KrProcessSharedExtensions -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
