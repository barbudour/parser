# DefaultFilterStrategy - класс
Стратегия, определяющая контекст фильтрации расширений перед выполнением
цепочки экземпляров расширений посредством политики
[IFilterPolicy](T_Tessa_Extensions_IFilterPolicy.htm). Если указанная политика
не зарегистрирована, то контекст фильтрации устанавливается равным null. Все
методы объекта являются потокобезопасными.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class DefaultFilterStrategy : IExtensionStrategy
VB __Копировать
     Public NotInheritable Class DefaultFilterStrategy
    	Implements IExtensionStrategy
C++ __Копировать
     public ref class DefaultFilterStrategy sealed : IExtensionStrategy
F# __Копировать
     [<SealedAttribute>]
    type DefaultFilterStrategy = 
        class
            interface IExtensionStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DefaultFilterStrategy
Implements
    [IExtensionStrategy](T_Tessa_Extensions_IExtensionStrategy.htm)
##  __Конструкторы
[DefaultFilterStrategy](M_Tessa_Extensions_DefaultFilterStrategy__ctor.htm)|
Инициализирует новый экземпляр класса DefaultFilterStrategy  
---|---  
##  __Свойства
[Instance](P_Tessa_Extensions_DefaultFilterStrategy_Instance.htm)| Экземпляр
класса.  
---|---  
##  __Методы
[ApplyAsync](M_Tessa_Extensions_DefaultFilterStrategy_ApplyAsync.htm)|
Применяет стратегию для заданного контекста, при этом при необходимости
изменяется контекст.  
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
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
