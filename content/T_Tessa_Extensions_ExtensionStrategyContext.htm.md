# ExtensionStrategyContext - класс
Контекст стратегии контейнера с расширениями
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm).
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ExtensionStrategyContext : IExtensionStrategyContext
VB __Копировать
     Public NotInheritable Class ExtensionStrategyContext
    	Implements IExtensionStrategyContext
C++ __Копировать
     public ref class ExtensionStrategyContext sealed : IExtensionStrategyContext
F# __Копировать
     [<SealedAttribute>]
    type ExtensionStrategyContext = 
        class
            interface IExtensionStrategyContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ExtensionStrategyContext
Implements
    [IExtensionStrategyContext](T_Tessa_Extensions_IExtensionStrategyContext.htm)
##  __Конструкторы
[ExtensionStrategyContext](M_Tessa_Extensions_ExtensionStrategyContext__ctor.htm)|
Создаёт экземпляр класса с указанием ключа, используемого для идентификации
типа расширения.  
---|---  
## __Свойства
[BuildKey](P_Tessa_Extensions_ExtensionStrategyContext_BuildKey.htm)|  Ключ,
используемый для идентификации типа расширения. Возвращаемое значение никогда
не равно null.  
---|---  
[ConcreteContexts](P_Tessa_Extensions_ExtensionStrategyContext_ConcreteContexts.htm)|
Список контекстов для экземпляров расширений, доступных на этапе
упорядочивания цепочки типов расширений, или null на прочих этапах.  
[Exception](P_Tessa_Extensions_ExtensionStrategyContext_Exception.htm)|
Исключение, возникшее в процессе выполнения метода расширения, или null, если
метод ещё не был выполнен или расширение не выбросило исключение.  
[ExceptionHandlingMode](P_Tessa_Extensions_ExtensionStrategyContext_ExceptionHandlingMode.htm)|
Режим обработки исключений, возникающий в методах расширений. Может быть
изменён в т.ч. в методе
[Tessa.Extensions.IExtensionTraceListener.NotifyException].  
[Executed](P_Tessa_Extensions_ExtensionStrategyContext_Executed.htm)|  Признак
того, что метод экземпляра расширения не будет выполнен стандартным образом,
т.к. либо он уже был выполнен, либо его выполнение не требуется.  
[ExecutionContext](P_Tessa_Extensions_ExtensionStrategyContext_ExecutionContext.htm)|
Параметр метода, выполняемого для экземпляра расширения.  
[ExecutionKey](P_Tessa_Extensions_ExtensionStrategyContext_ExecutionKey.htm)|
Ключ, используемый для идентификации метода, выполняемого для экземпляра
расширения.  
[FilterContext](P_Tessa_Extensions_ExtensionStrategyContext_FilterContext.htm)|
Контекст фильтрации, используемый перед выполнением цепочки экземпляров
расширений.  
[Policies](P_Tessa_Extensions_ExtensionStrategyContext_Policies.htm)|
Контейнер политик, ассоциированных с типом или экземпяром расширения.
Возвращаемое значение никогда не равно null.  
[ResolvedExtension](P_Tessa_Extensions_ExtensionStrategyContext_ResolvedExtension.htm)|
Полученный экземпляр расширения или null, если экземпляр ещё не был получен.  
[ResolveKey](P_Tessa_Extensions_ExtensionStrategyContext_ResolveKey.htm)|
Ключ, используемый для идентификации экземпляра расширения, или null, если
контекст построен для типа расширения, а не для экземпляра.  
[StopExecution](P_Tessa_Extensions_ExtensionStrategyContext_StopExecution.htm)|
Признак того, что запрошена остановка выполнения цепочки расширений. Т.е.
текущее выполняемое расширение станет последним. При этом ошибок не
выбрасывается.  
[TraceContext](P_Tessa_Extensions_ExtensionStrategyContext_TraceContext.htm)|
Контекст трассировки, используемый для хранения информации между сообщениями
трассировки.  
##  __Методы
[Clone](M_Tessa_Extensions_ExtensionStrategyContext_Clone.htm)|  Выполняет
поверхностную копию объекта всех полей объекта, кроме контейнера политик
[Tessa.Extensions.IExtensionStrategyContext.Policies], для которого
копирование зависит от shallowClone.  
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
