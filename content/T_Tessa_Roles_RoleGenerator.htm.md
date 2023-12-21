# RoleGenerator - класс
Генератор метаролей.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [DataContractAttribute]
    [TableAttribute("RoleGenerators", IsColumnAttributeRequired = false)]
    public sealed class RoleGenerator : NamedEntry, 
    	IRoleSchedulingProvider, IRoleLastErrorContainer
VB __Копировать
    <DataContractAttribute>
    <TableAttribute("RoleGenerators", IsColumnAttributeRequired := false)>
    Public NotInheritable Class RoleGenerator
    	Inherits NamedEntry
    	Implements IRoleSchedulingProvider, IRoleLastErrorContainer
C++ __Копировать
    [DataContractAttribute]
    [TableAttribute(L"RoleGenerators", IsColumnAttributeRequired = false)]
    public ref class RoleGenerator sealed : public NamedEntry, 
    	IRoleSchedulingProvider, IRoleLastErrorContainer
F# __Копировать
     [<SealedAttribute>]
    [<DataContractAttribute>]
    [<TableAttribute("RoleGenerators", IsColumnAttributeRequired = false)>]
    type RoleGenerator = 
        class
            inherit NamedEntry
            interface IRoleSchedulingProvider
            interface IRoleLastErrorContainer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NamedEntry](T_Tessa_Platform_NamedEntry.htm) __ RoleGenerator
Implements
    [IRoleLastErrorContainer](T_Tessa_Roles_IRoleLastErrorContainer.htm), [IRoleSchedulingProvider](T_Tessa_Roles_IRoleSchedulingProvider.htm)
##  __Конструкторы
[RoleGenerator](M_Tessa_Roles_RoleGenerator__ctor.htm)| Инициализирует новый
экземпляр класса RoleGenerator  
---|---  
##  __Свойства
[CronScheduling](P_Tessa_Roles_RoleGenerator_CronScheduling.htm)|  Строка
Cron, определяющая расписание генерации метаролей, или null, если расписание
генерации определяется не через Cron.  
---|---  
[HasError](P_Tessa_Roles_RoleGenerator_HasError.htm)|  Признак того, что
генератор метаролей имеет сообщение о последней ошибке, возникшей при
генерации.  
[ID](P_Tessa_Platform_NamedEntry_ID.htm)| Идентификатор объекта.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
[LastErrorDate](P_Tessa_Roles_RoleGenerator_LastErrorDate.htm)|
Дата последней ошибки, возникшей в генераторе, или null, если ошибки не
возникало.
Дата должна указываться в формате UTC (Coordinated Universal Time).  
[LastErrorText](P_Tessa_Roles_RoleGenerator_LastErrorText.htm)|  Сообщение о
последней ошибке, возникшей при генерации, или null, если ошибки не возникало.  
[LastException](P_Tessa_Roles_RoleGenerator_LastException.htm)|  Последняя
ошибка при генерации, или null, если ошибки не возникало.  
[Modified](P_Tessa_Roles_RoleGenerator_Modified.htm)|  Дата и время последнего
изменения роли.  
[ModifiedBy](P_Tessa_Roles_RoleGenerator_ModifiedBy.htm)|  Пользователь,
последним выполнивший изменение генератора метаролей.  
[ModifiedByID](P_Tessa_Roles_RoleGenerator_ModifiedByID.htm)|  Идентификатор
пользователя, последним выполнившего изменение роли. Если генератор метаролей
был изменён системой, то используйте метод
[SetModifiedBySystem()](M_Tessa_Roles_RoleGenerator_SetModifiedBySystem.htm).  
[ModifiedByName](P_Tessa_Roles_RoleGenerator_ModifiedByName.htm)|  Имя
пользователя, последним выполнившего изменение роли. Если генератор метаролей
был изменён системой, то используйте метод
[SetModifiedBySystem()](M_Tessa_Roles_RoleGenerator_SetModifiedBySystem.htm).  
[Name](P_Tessa_Platform_NamedEntry_Name.htm)| Отображаемое имя объекта.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
[PeriodScheduling](P_Tessa_Roles_RoleGenerator_PeriodScheduling.htm)|
Интервал в секундах, определяющий период генерации метаролей, или null, если
расписание генерации определяется не через период.  
[ScheduleAtLaunch](P_Tessa_Roles_RoleGenerator_ScheduleAtLaunch.htm)|
Запланировать пересчёт при запуске сервиса Chronos.  
[SchedulingType](P_Tessa_Roles_RoleGenerator_SchedulingType.htm)|  Способ
указания расписания для пересчёта состава роли.  
[SqlText](P_Tessa_Roles_RoleGenerator_SqlText.htm)|  Текст SQL-запроса
генератора метаролей.  
## __Методы
[Equals(INamedEntry)](M_Tessa_Platform_NamedEntry_Equals_1.htm)| Сравнивает
текущий объект с заданным.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
---|---  
[Equals(Object)](M_Tessa_Platform_NamedEntry_Equals.htm)| Сравнивает текущий
объект с заданным.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Platform_NamedEntry_GetHashCode.htm)| Возвращает хеш-код
объекта.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
[GetName](M_Tessa_Platform_NamedEntry_GetName.htm)|  Возвращает имя объекта.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
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
[SetModifiedBySystem](M_Tessa_Roles_RoleGenerator_SetModifiedBySystem.htm)|
Устанавливает свойства
[ModifiedByID](P_Tessa_Roles_RoleGenerator_ModifiedByID.htm) и
[ModifiedByName](P_Tessa_Roles_RoleGenerator_ModifiedByName.htm) таким
образом, чтобы установить, что генератор метаролей был изменён системой.  
[ToString](M_Tessa_Platform_NamedEntry_ToString.htm)| Возвращает строковое
представление объекта.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
[UpdateFromAssociations](M_Tessa_Roles_RoleGenerator_UpdateFromAssociations.htm)|
Обновляет значения ссылочных полей из всех объектов-ассоциаций, на которые
установлены ссылки.  
(Переопределяет
[NamedEntry.UpdateFromAssociations()](M_Tessa_Platform_NamedEntry_UpdateFromAssociations.htm))  
##  __Методы расширения
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
[Tessa.Roles - пространство имён](N_Tessa_Roles.htm)
