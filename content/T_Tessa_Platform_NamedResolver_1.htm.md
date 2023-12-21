# NamedResolver<TValue> \- класс
Объект, используемый для запросов типов сервисов по именам.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class NamedResolver<TValue> : Resolver<string, TValue>
    where TValue : class
VB __Копировать
     Public MustInherit Class NamedResolver(Of TValue As Class)
    	Inherits Resolver(Of String, TValue)
C++ __Копировать
    generic<typename TValue>
    where TValue : ref class
    public ref class NamedResolver abstract : public Resolver<String^, TValue>
F# __Копировать
     [<AbstractClassAttribute>]
    type NamedResolver<'TValue when 'TValue : not struct> = 
        class
            inherit Resolver<string, 'TValue>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Resolver](T_Tessa_Platform_Resolver_2.htm)<[String](https://learn.microsoft.com/dotnet/api/system.string), TValue> __ NamedResolver<TValue>
Derived
[Tessa.Extensions.Platform.Server.Cards.CardStrictSecurityResolver](T_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurityResolver.htm)
[Tessa.Platform.Runtime.AuthenticationServiceResolver](T_Tessa_Platform_Runtime_AuthenticationServiceResolver.htm)
#### Параметры типа
TValue
    Интерфейс запрашиваемого сервиса. Должен быть ссылочным типом.
##  __Конструкторы
[NamedResolver<TValue>](M_Tessa_Platform_NamedResolver_1__ctor.htm)|  Создаёт
экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[TypesByKey](P_Tessa_Platform_Resolver_2_TypesByKey.htm)|  Типы значений,
запрашиваемых из
[UnityContainer](P_Tessa_Platform_Resolver_2_UnityContainer.htm) по имени.
Если объект отсутствует, то типы запрашиваться не будут.  
(Унаследован от [Resolver<TKey, TValue>](T_Tessa_Platform_Resolver_2.htm))  
---|---  
[UnityContainer](P_Tessa_Platform_Resolver_2_UnityContainer.htm)|  Контейнер
Unity, используемый для получения зарегистрированных значений.  
(Унаследован от [Resolver<TKey, TValue>](T_Tessa_Platform_Resolver_2.htm))  
##  __Методы
[AutoResolveKey](M_Tessa_Platform_Resolver_2_AutoResolveKey.htm)|
Автоматически вычисляет значение ключа из переданного типа, если ключ не
задан. Вызывается перед методом FixKey. Возвращает вычисленное значение ключа,
если это возможно, или текущее значение, если невозможно. Исключение не
выбрасывает. По умолчанию возвращается исходный объект без изменений.  
(Унаследован от [Resolver<TKey, TValue>](T_Tessa_Platform_Resolver_2.htm))  
---|---  
[Clear](M_Tessa_Platform_Resolver_2_Clear.htm)| Удаляет информацию по всем
выполненным регистрациям.  
(Унаследован от [Resolver<TKey, TValue>](T_Tessa_Platform_Resolver_2.htm))  
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
[FixKey](M_Tessa_Platform_NamedResolver_1_FixKey.htm)|  Проверяет ключ на
валидность. Вызывается после метода AutoResolveKey. Возвращает исправленное
значение ключа, если это возможно, или исключение, если невозможно. По
умолчанию возвращается исходный объект без изменений.  
(Переопределяет [Resolver<TKey,
TValue>.FixKey(TKey)](M_Tessa_Platform_Resolver_2_FixKey.htm))  
[GetAllKeys](M_Tessa_Platform_Resolver_2_GetAllKeys.htm)| Возвращает список
всех зарегистрированных ключей.  
(Унаследован от [Resolver<TKey, TValue>](T_Tessa_Platform_Resolver_2.htm))  
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
(Унаследован от [Resolver<TKey, TValue>](T_Tessa_Platform_Resolver_2.htm))  
[Register<TConcrete>(TKey)](M_Tessa_Platform_Resolver_2_Register__1.htm)|
Регистрирует тип объекта по заданному ключу. Резолв возможен только для
зарегистрированных типов. Обычно резолв сервиса выполняется из контейнера
Unity каждый раз при вызове этого метода, при этом объект запрашивается по
зарегистрированному типу (классу) без имени в контейнере.  
(Унаследован от [Resolver<TKey, TValue>](T_Tessa_Platform_Resolver_2.htm))  
[Remove](M_Tessa_Platform_Resolver_2_Remove.htm)| Удаляет информацию по
регистрации с заданным ключом.  
(Унаследован от [Resolver<TKey, TValue>](T_Tessa_Platform_Resolver_2.htm))  
[Resolve](M_Tessa_Platform_Resolver_2_Resolve.htm)|  Выполняет резолв
экземпляра заданного сервиса по заданному ключу. Если сервис не был
зарегистрирован, то выбрасывается исключение
[Unity.ResolutionFailedException]. Обычно резолв сервиса выполняется из
контейнера Unity каждый раз при вызове этого метода, при этом объект
запрашивается по зарегистрированному типу (классу) без имени в контейнере.  
(Унаследован от [Resolver<TKey, TValue>](T_Tessa_Platform_Resolver_2.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryResolve](M_Tessa_Platform_Resolver_2_TryResolve.htm)|  Выполняет резолв
экземпляра заданного сервиса по имени. Если сервис не был зарегистрирован, то
возвращает null. Обычно резолв сервиса выполняется из контейнера Unity каждый
раз при вызове этого метода, при этом объект запрашивается по
зарегистрированному типу (классу) без имени в контейнере.  
(Унаследован от [Resolver<TKey, TValue>](T_Tessa_Platform_Resolver_2.htm))  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
