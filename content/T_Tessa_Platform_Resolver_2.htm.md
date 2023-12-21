# Resolver<TKey, TValue> \- класс
Объект, используемый для запросов типов сервисов по ключу, например, по имени.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class Resolver<TKey, TValue> : IResolver<TKey, TValue>
    where TValue : class
VB __Копировать
     Public MustInherit Class Resolver(Of TKey, TValue As Class)
    	Implements IResolver(Of TKey, TValue)
C++ __Копировать
    generic<typename TKey, typename TValue>
    where TValue : ref class
    public ref class Resolver abstract : IResolver<TKey, TValue>
F# __Копировать
     [<AbstractClassAttribute>]
    type Resolver<'TKey, 'TValue when 'TValue : not struct> = 
        class
            interface IResolver<'TKey, 'TValue>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ Resolver<TKey, TValue>
Derived
[Tessa.Notices.Sources.NotificationEmailSourceResolver](T_Tessa_Notices_Sources_NotificationEmailSourceResolver.htm)
[Tessa.Notices.Sources.NotificationRecipientsSourceResolver](T_Tessa_Notices_Sources_NotificationRecipientsSourceResolver.htm)
[Tessa.Platform.Conditions.ConditionSourceHandlerResolver](T_Tessa_Platform_Conditions_ConditionSourceHandlerResolver.htm)
[Tessa.Platform.NamedResolver<TValue>](T_Tessa_Platform_NamedResolver_1.htm)
[Tessa.Platform.Storage.Mapping.StorageMappingResolver](T_Tessa_Platform_Storage_Mapping_StorageMappingResolver.htm)
[Tessa.UI.Cards.BlockTypeResolver](T_Tessa_UI_Cards_BlockTypeResolver.htm)
[Tessa.UI.Cards.ControlTypeResolver](T_Tessa_UI_Cards_ControlTypeResolver.htm)
[Tessa.UI.Cards.FormTypeResolver](T_Tessa_UI_Cards_FormTypeResolver.htm)
[Tessa.UI.Cards.TypeExtensionTypeResolver](T_Tessa_UI_Cards_TypeExtensionTypeResolver.htm)
[Tessa.UI.Cards.ValidatorTypeResolver](T_Tessa_UI_Cards_ValidatorTypeResolver.htm)
[Tessa.Workflow.BPMN.WorkflowEngineBPMNObjectConverterResolver](T_Tessa_Workflow_BPMN_WorkflowEngineBPMNObjectConverterResolver.htm)
Подробнее __Less __
Implements
    [IResolver](T_Tessa_Platform_IResolver_2.htm)<TKey, TValue>
#### Параметры типа
TKey
    Ключ для запроса значения.
TValue
    Интерфейс запрашиваемого сервиса. Должен быть ссылочным типом.
##  __Конструкторы
[Resolver<TKey, TValue>](M_Tessa_Platform_Resolver_2__ctor.htm)|  Создаёт
экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[TypesByKey](P_Tessa_Platform_Resolver_2_TypesByKey.htm)|  Типы значений,
запрашиваемых из
[UnityContainer](P_Tessa_Platform_Resolver_2_UnityContainer.htm) по имени.
Если объект отсутствует, то типы запрашиваться не будут.  
---|---  
[UnityContainer](P_Tessa_Platform_Resolver_2_UnityContainer.htm)|  Контейнер
Unity, используемый для получения зарегистрированных значений.  
## __Методы
[AutoResolveKey](M_Tessa_Platform_Resolver_2_AutoResolveKey.htm)|
Автоматически вычисляет значение ключа из переданного типа, если ключ не
задан. Вызывается перед методом FixKey. Возвращает вычисленное значение ключа,
если это возможно, или текущее значение, если невозможно. Исключение не
выбрасывает. По умолчанию возвращается исходный объект без изменений.  
---|---  
[Clear](M_Tessa_Platform_Resolver_2_Clear.htm)| Удаляет информацию по всем
выполненным регистрациям.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FixKey](M_Tessa_Platform_Resolver_2_FixKey.htm)|  Проверяет ключ на
валидность. Вызывается после метода AutoResolveKey. Возвращает исправленное
значение ключа, если это возможно, или исключение, если невозможно. По
умолчанию возвращается исходный объект без изменений.  
[GetAllKeys](M_Tessa_Platform_Resolver_2_GetAllKeys.htm)| Возвращает список
всех зарегистрированных ключей.  
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
[Register(Type, TKey)](M_Tessa_Platform_Resolver_2_Register.htm)|
Регистрирует тип объекта по заданному ключу. Резолв возможен только для
зарегистрированных типов. Обычно резолв сервиса выполняется из контейнера
Unity каждый раз при вызове этого метода, при этом объект запрашивается по
зарегистрированному типу (классу) без имени в контейнере.  
[Register<TConcrete>(TKey)](M_Tessa_Platform_Resolver_2_Register__1.htm)|
Регистрирует тип объекта по заданному ключу. Резолв возможен только для
зарегистрированных типов. Обычно резолв сервиса выполняется из контейнера
Unity каждый раз при вызове этого метода, при этом объект запрашивается по
зарегистрированному типу (классу) без имени в контейнере.  
[Remove](M_Tessa_Platform_Resolver_2_Remove.htm)| Удаляет информацию по
регистрации с заданным ключом.  
[Resolve](M_Tessa_Platform_Resolver_2_Resolve.htm)|  Выполняет резолв
экземпляра заданного сервиса по заданному ключу. Если сервис не был
зарегистрирован, то выбрасывается исключение
[Unity.ResolutionFailedException]. Обычно резолв сервиса выполняется из
контейнера Unity каждый раз при вызове этого метода, при этом объект
запрашивается по зарегистрированному типу (классу) без имени в контейнере.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryResolve](M_Tessa_Platform_Resolver_2_TryResolve.htm)|  Выполняет резолв
экземпляра заданного сервиса по имени. Если сервис не был зарегистрирован, то
возвращает null. Обычно резолв сервиса выполняется из контейнера Unity каждый
раз при вызове этого метода, при этом объект запрашивается по
зарегистрированному типу (классу) без имени в контейнере.  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
