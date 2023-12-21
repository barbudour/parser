# ScopeContext<TContext> \- класс
Область операции с контекстом.
## __Definition
 **Пространство имён:** [Tessa.Platform.Scopes](N_Tessa_Platform_Scopes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ScopeContext<TContext> : IScopeContext<TContext>
VB __Копировать
     Public NotInheritable Class ScopeContext(Of TContext)
    	Implements IScopeContext(Of TContext)
C++ __Копировать
    generic<typename TContext>
    public ref class ScopeContext sealed : IScopeContext<TContext>
F# __Копировать
     [<SealedAttribute>]
    type ScopeContext<'TContext> = 
        class
            interface IScopeContext<'TContext>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ScopeContext<TContext>
Implements
    [IScopeContext](T_Tessa_Platform_Scopes_IScopeContext_1.htm)<TContext>
#### Параметры типа
TContext
    Тип контекста операции.
##  __Свойства
[Context](P_Tessa_Platform_Scopes_ScopeContext_1_Context.htm)| Контекст,
установленный внутри текущей операции.  
---|---  
[Current](P_Tessa_Platform_Scopes_ScopeContext_1_Current.htm)|  Объект,
содержащий текущий контекст, или null, если текущий контекст отсутствует.  
[HasContext](P_Tessa_Platform_Scopes_ScopeContext_1_HasContext.htm)| Признак
того, что код исполняется внутри области операции, для которой определён
контекст.  
[Instance](P_Tessa_Platform_Scopes_ScopeContext_1_Instance.htm)| Экземпляр
класса.  
[Parent](P_Tessa_Platform_Scopes_ScopeContext_1_Parent.htm)|  Объект,
содержащий родительский контекст, или null, если текущий или родительский
контексты отсутствуют.  
## __Методы
[Create](M_Tessa_Platform_Scopes_ScopeContext_1_Create.htm)| Создаёт экземпляр
области операции, в пределах которой будет установлен заданный контекст.  
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
[Tessa.Platform.Scopes - пространство имён](N_Tessa_Platform_Scopes.htm)
