# SatelliteTypeDescriptor - класс
Объект с описанием типа сателлита.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards.Satellites](N_Tessa_Extensions_Platform_Server_Cards_Satellites.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SatelliteTypeDescriptor : IRegistryItem<Guid>
VB __Копировать
     Public NotInheritable Class SatelliteTypeDescriptor
    	Implements IRegistryItem(Of Guid)
C++ __Копировать
     public ref class SatelliteTypeDescriptor sealed : IRegistryItem<Guid>
F# __Копировать
     [<SealedAttribute>]
    type SatelliteTypeDescriptor = 
        class
            interface IRegistryItem<Guid>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SatelliteTypeDescriptor
Implements
    [IRegistryItem](T_Tessa_Platform_IRegistryItem_1.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __Конструкторы
[SatelliteTypeDescriptor](M_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor__ctor.htm)|
Инициализирует новый экземпляр класса SatelliteTypeDescriptor  
---|---  
##  __Свойства
[AllowDeleteFromClient](P_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor_AllowDeleteFromClient.htm)|
Определяет, доступно ли удаление сателлита с клиента.  
---|---  
[AllowGetFromClient](P_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor_AllowGetFromClient.htm)|
Определяет, доступна ли загрузка сателлита с клиента.  
[AllowStoreFromClient](P_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor_AllowStoreFromClient.htm)|
Определяет, доступно ли сохранение сателлита с клиента.  
[CopySatelliteOnCardCopy](P_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor_CopySatelliteOnCardCopy.htm)|
Определяет, нужно ли копировать данный сателлит при копировании основной
карточки.  
[HandlerType](P_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor_HandlerType.htm)|
Тип хендлера для сателлита. Должен реализовывать интерфейс
[ISatelliteHandler](T_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_ISatelliteHandler.htm)  
[ID](P_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor_ID.htm)|
Идентификатор объекта, по которому выполняется регистрация в реестре.  
[IgnoreGetPrepare](P_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor_IgnoreGetPrepare.htm)|
Определяет, что при загрузке данного типа сателлита не будут производиться
методы подготовки сателлита по основной карточке. При наличии данного флага
следующие настройки типа сателлита и его обработчика игнорируются: 1)
[LoadMainCardFiles](P_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor_LoadMainCardFiles.htm)
2) [PrepareSatelliteForGetAsync(ICardGetExtensionContext, Card, Guid,
Nullable<Guid>, Func<CancellationToken,
ValueTask<Card>>)](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_ISatelliteHandler_PrepareSatelliteForGetAsync.htm)
3) [GetExternalFileSourcesAsync(ICardGetExtensionContext, Card, Guid,
Nullable<Guid>)](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_ISatelliteHandler_GetExternalFileSourcesAsync.htm)  
[IgnoreStoreExtensions](P_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor_IgnoreStoreExtensions.htm)|
Определяет, что данный тип сателлита игнорирует стандартные расширение на
сохранение сателлита.  
[IsDeferredStore](P_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor_IsDeferredStore.htm)|
Определяет, что сателлит не будет сохранен при его загрузке.  
[IsSingleton](P_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor_IsSingleton.htm)|
Определяет, должен ли данный тип сателлита быть синглтоном по отношению к
основной карточке.  
[IsTaskSatellite](P_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor_IsTaskSatellite.htm)|
Определяет, относится ли сателлит к карточке или заданию карточки.  
[LoadMainCardFiles](P_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor_LoadMainCardFiles.htm)|
Определяет, нужно ли загружать файлы основной карточки в карточку сателлита.  
[SatelliteTypeID](P_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor_SatelliteTypeID.htm)|
Идентификатор типа карточки сателлита.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[AutoSatelliteType](F_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor_AutoSatelliteType.htm)|
Тип сателлита, который не зарегистрирован в
[ISatelliteTypeRegistry](T_Tessa_Extensions_Platform_Server_Cards_Satellites_ISatelliteTypeRegistry.htm),
но определяется по наличию секции Satellites в типе карточки.  
---|---  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Platform.Server.Cards.Satellites - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards_Satellites.htm)
