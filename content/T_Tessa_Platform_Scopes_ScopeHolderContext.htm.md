# ScopeHolderContext - класс
Контекст объекта, выполняющего удержание наследуемых контекстов. Например,
удержание автоматически происходит при выполнении расширений
[IExtensionExecutor<TExtension>](T_Tessa_Extensions_IExtensionExecutor_1.htm),
а также "между" цепочками расширений в API карточек.
## __Definition
 **Пространство имён:** [Tessa.Platform.Scopes](N_Tessa_Platform_Scopes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ScopeHolderContext : IScopeHolderContext, 
    	IDisposable
VB __Копировать
     Public NotInheritable Class ScopeHolderContext
    	Implements IScopeHolderContext, IDisposable
C++ __Копировать
     public ref class ScopeHolderContext sealed : IScopeHolderContext, 
    	IDisposable
F# __Копировать
     [<SealedAttribute>]
    type ScopeHolderContext = 
        class
            interface IScopeHolderContext
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ScopeHolderContext
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IScopeHolderContext](T_Tessa_Platform_Scopes_IScopeHolderContext.htm)
##  __Конструкторы
[ScopeHolderContext](M_Tessa_Platform_Scopes_ScopeHolderContext__ctor.htm)|
Инициализирует новый экземпляр класса ScopeHolderContext  
---|---  
##  __Свойства
[Current](P_Tessa_Platform_Scopes_ScopeHolderContext_Current.htm)|  Текущий
контекст
[IScopeHolderContext](T_Tessa_Platform_Scopes_IScopeHolderContext.htm).
Возвращает null, если контекст отсутствует.  
---|---  
[HasCurrent](P_Tessa_Platform_Scopes_ScopeHolderContext_HasCurrent.htm)|
Признак того, что текущий код выполняется внутри операции с контекстом
[IScopeHolderContext](T_Tessa_Platform_Scopes_IScopeHolderContext.htm), а
свойство [Current](P_Tessa_Platform_Scopes_ScopeHolderContext_Current.htm)
ссылается на null.  
## __Методы
[Create](M_Tessa_Platform_Scopes_ScopeHolderContext_Create.htm)|  Создаёт
область удержания доступных контекстов
[IScopeHolderContext](T_Tessa_Platform_Scopes_IScopeHolderContext.htm). Если
область уже создана, то она не создаётся повторно. Обязательно заключите в
using результат вызова метода.  
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
[Set](M_Tessa_Platform_Scopes_ScopeHolderContext_Set.htm)|  Устанавливает
объект, удерживаемый в контексте для заданного типа, или null, если объект
удаляется.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGet](M_Tessa_Platform_Scopes_ScopeHolderContext_TryGet.htm)|  Возвращает
объект, удерживаемый в контексте для заданного типа, или null, если объект
отсутствует.  
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
[Tessa.Platform.Scopes - пространство имён](N_Tessa_Platform_Scopes.htm)
