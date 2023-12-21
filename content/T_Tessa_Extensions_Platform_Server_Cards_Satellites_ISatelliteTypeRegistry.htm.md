# ISatelliteTypeRegistry - интерфейс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards.Satellites](N_Tessa_Extensions_Platform_Server_Cards_Satellites.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISatelliteTypeRegistry : IRegistry<Guid, SatelliteTypeDescriptor>
VB __Копировать
     Public Interface ISatelliteTypeRegistry
    	Inherits IRegistry(Of Guid, SatelliteTypeDescriptor)
C++ __Копировать
     public interface class ISatelliteTypeRegistry : IRegistry<Guid, SatelliteTypeDescriptor^>
F# __Копировать
     type ISatelliteTypeRegistry = 
        interface
            interface IRegistry<Guid, SatelliteTypeDescriptor>
        end
Implements
    [IRegistry](T_Tessa_Platform_IRegistry_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), [SatelliteTypeDescriptor](T_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor.htm)>
##  __Методы
[Get](M_Tessa_Platform_IRegistry_2_Get.htm)| Возвращает объект,
зарегистрированный в реестре по заданному идентификатору.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
---|---  
[GetAll](M_Tessa_Platform_IRegistry_2_GetAll.htm)| Возвращает все
зарегистрированные в реестре объекты.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
[GetSatelliteHandler](M_Tessa_Extensions_Platform_Server_Cards_Satellites_ISatelliteTypeRegistry_GetSatelliteHandler.htm)|
Метод для получения обработчика сателлита по его дескриптору, или null, если
обработчик для данного типа сателлита не предусмотрен.  
[IsDefined(TIdentifier)](M_Tessa_Platform_IRegistry_2_IsDefined.htm)|
Возвращает признак того, что в реестре был зарегистрирован объект по заданному
идентификатору.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
[IsDefined(TItem)](M_Tessa_Platform_IRegistry_2_IsDefined_1.htm)| Возвращает
признак того, что заданный объект был зарегистрирован в реестре.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
[Register](M_Tessa_Platform_IRegistry_2_Register.htm)| Регистрирует объект по
его идентификатору. Метод замещает предыдущую регистрацию при её наличии.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
[TryGet](M_Tessa_Platform_IRegistry_2_TryGet.htm)|  Возвращает объект в
параметре result, зарегистрированный в реестре по заданному идентификатору.
Метод возвращает false, если объект отсутствует в реестре.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
[TryGetExtendedAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_ISatelliteTypeRegistry_TryGetExtendedAsync.htm)|
Метод для получения дескриптора типа сателлита. Возвращает зарегистрированный
тип сателлита или
[AutoSatelliteType](F_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor_AutoSatelliteType.htm),
если в типе карточки есть секция Satellites.  
## __См. также
#### Ссылки
[Tessa.Extensions.Platform.Server.Cards.Satellites - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards_Satellites.htm)
