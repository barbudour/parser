# IValidationKeyRegistry - интерфейс
Реестр ключей валидации
[ValidationKey](T_Tessa_Platform_Validation_ValidationKey.htm).
## __Definition
 **Пространство имён:**
[Tessa.Platform.Validation](N_Tessa_Platform_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IValidationKeyRegistry : INamedRegistry<ValidationKey>, 
    	IRegistry<Guid, ValidationKey>
VB __Копировать
     Public Interface IValidationKeyRegistry
    	Inherits INamedRegistry(Of ValidationKey), IRegistry(Of Guid, ValidationKey)
C++ __Копировать
     public interface class IValidationKeyRegistry : INamedRegistry<ValidationKey^>, 
    	IRegistry<Guid, ValidationKey^>
F# __Копировать
     type IValidationKeyRegistry = 
        interface
            interface INamedRegistry<ValidationKey>
            interface IRegistry<Guid, ValidationKey>
        end
Implements
    [INamedRegistry](T_Tessa_Platform_INamedRegistry_1.htm)<[ValidationKey](T_Tessa_Platform_Validation_ValidationKey.htm)>, [IRegistry](T_Tessa_Platform_IRegistry_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), [ValidationKey](T_Tessa_Platform_Validation_ValidationKey.htm)>
##  __Методы
[Get(TIdentifier)](M_Tessa_Platform_IRegistry_2_Get.htm)| Возвращает объект,
зарегистрированный в реестре по заданному идентификатору.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
---|---  
[Get(String)](M_Tessa_Platform_INamedRegistry_1_Get.htm)| Возвращает объект,
зарегистрированный в реестре по заданному имени.  
(Унаследован от
[INamedRegistry<TItem>](T_Tessa_Platform_INamedRegistry_1.htm))  
[GetAll](M_Tessa_Platform_IRegistry_2_GetAll.htm)| Возвращает все
зарегистрированные в реестре объекты.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
[IsDefined(TIdentifier)](M_Tessa_Platform_IRegistry_2_IsDefined.htm)|
Возвращает признак того, что в реестре был зарегистрирован объект по заданному
идентификатору.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
[IsDefined(TItem)](M_Tessa_Platform_IRegistry_2_IsDefined_1.htm)| Возвращает
признак того, что заданный объект был зарегистрирован в реестре.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
[IsDefined(String)](M_Tessa_Platform_INamedRegistry_1_IsDefined.htm)|
Возвращает признак того, что в реестре был зарегистрирован объект по заданному
имени.  
(Унаследован от
[INamedRegistry<TItem>](T_Tessa_Platform_INamedRegistry_1.htm))  
[Register](M_Tessa_Platform_IRegistry_2_Register.htm)| Регистрирует объект по
его идентификатору. Метод замещает предыдущую регистрацию при её наличии.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
[TryGet](M_Tessa_Platform_IRegistry_2_TryGet.htm)|  Возвращает объект в
параметре result, зарегистрированный в реестре по заданному идентификатору.
Метод возвращает false, если объект отсутствует в реестре.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Validation - пространство
имён](N_Tessa_Platform_Validation.htm)
