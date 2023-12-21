# AccessPolicy<TAccessSubject, TContext> \- класс
Универсальный класс политики проверки доступности объектов. Используется для
проверки наличия доступа к объекту через список правил
[IAccessRule<TAccessSubject,
TMandatoryContext>](T_Tessa_Views_AccessPolicy_IAccessRule_2.htm) получаемых в
конструкторе класса. Правила доступности по умолчанию должны регистрироваться
в контейнере приложения. Базовая политика доступности с помощью контейнера
приложения поддерживает два вида правил. Правила не зависимые от субъекта
доступа и контекста должны быть реализованы как открытие обобщенные классы:
## __Пример
public class ConcreteRule<TAccessSubject, TContext> :
IAccessRule<TAccessSuject, TContext> { .... }
container.RegisterType(typeof(IAccessRule<,>), typeof(ConcreteRule<,>),
typeof(ConcreteRule<>).Name);
закрытие классы:
## __Пример
public class ConcreteRule: IAccessRule<ConcreteAccessSubject, ConcreteContext>
{ .... } container.RegisterType<IAccessRule<ConcreteAccessSubject,
ConcreteContext>, ConcreteRule>();
При получении политики IAccessPolicy<ConcreteAccessSubject, ConcreteContext>
из контейнера будут получены оба вида правил. Унаследование классы могут
использовать собственные типы правил и получать их из контейнера, через
конструктор отдельно от предыдущих двух типов и затем добавляя из в список
правил политики через [AddRules(IEnumerable<IAccessRule<TAccessSubject,
TContext>>)](M_Tessa_Views_AccessPolicy_IAccessPolicy_2_AddRules.htm) приводя
к базовому типу.
## __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class AccessPolicy<TAccessSubject, TContext> : IAccessPolicy<TAccessSubject, TContext>
VB __Копировать
     Public Class AccessPolicy(Of TAccessSubject, TContext)
    	Implements IAccessPolicy(Of TAccessSubject, TContext)
C++ __Копировать
    generic<typename TAccessSubject, typename TContext>
    public ref class AccessPolicy : IAccessPolicy<TAccessSubject, TContext>
F# __Копировать
     type AccessPolicy<'TAccessSubject, 'TContext> = 
        class
            interface IAccessPolicy<'TAccessSubject, 'TContext>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AccessPolicy<TAccessSubject, TContext>
Derived
[Tessa.Views.AccessPolicy.ViewAccessPolicy<TContext>](T_Tessa_Views_AccessPolicy_ViewAccessPolicy_1.htm)
[Tessa.Views.AccessPolicy.WorkplaceAccessPolicy<TContext>](T_Tessa_Views_AccessPolicy_WorkplaceAccessPolicy_1.htm)
Implements
    [IAccessPolicy](T_Tessa_Views_AccessPolicy_IAccessPolicy_2.htm)<TAccessSubject, TContext>
#### Параметры типа
TAccessSubject
     Тип объекта 
TContext
     Тип контекста 
## __Конструкторы
[AccessPolicy<TAccessSubject,
TContext>](M_Tessa_Views_AccessPolicy_AccessPolicy_2__ctor.htm)|
Инициализирует новый экземпляр класса AccessPolicy<TAccessSubject, TContext>  
---|---  
##  __Методы
[AddRules](M_Tessa_Views_AccessPolicy_AccessPolicy_2_AddRules.htm)|  Добавляет
правила в политику безопасности  
---|---  
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
[IsSatisfiedByAsync](M_Tessa_Views_AccessPolicy_AccessPolicy_2_IsSatisfiedByAsync.htm)|
Осуществляет проверку доступности элемента subject в соответствии с правилами
политик доступа.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.Views.AccessPolicy - пространство имён](N_Tessa_Views_AccessPolicy.htm)
