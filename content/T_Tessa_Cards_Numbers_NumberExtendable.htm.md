# NumberExtendable - класс
Базовый объект, выполняющий расширяемые действия с номером.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class NumberExtendable : INumberExtendable
VB __Копировать
     Public MustInherit Class NumberExtendable
    	Implements INumberExtendable
C++ __Копировать
     public ref class NumberExtendable abstract : INumberExtendable
F# __Копировать
     [<AbstractClassAttribute>]
    type NumberExtendable = 
        class
            interface INumberExtendable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberExtendable
Derived
[Tessa.Cards.Numbers.NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers.NumberComposer](T_Tessa_Cards_Numbers_NumberComposer.htm)
Implements
    [INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm)
##  __Конструкторы
[NumberExtendable](M_Tessa_Cards_Numbers_NumberExtendable__ctor.htm)|
Инициализирует новый экземпляр класса NumberExtendable  
---|---  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[MethodReturnedNull](M_Tessa_Cards_Numbers_NumberExtendable_MethodReturnedNull.htm)|
Создаёт и возвращает исключение, которое вызывается в случае, когда
перегруженный виртуальный метод вернул null, хотя он не должен был возвращать
null.  
[NotifyAfterEventAsync](M_Tessa_Cards_Numbers_NumberExtendable_NotifyAfterEventAsync.htm)|
Выполняет постобработку события, происходящего с номером. Это предоставляет
возможность изменить результат обработанного события или сохранить результат
во внешнем хранилище.  
[NotifyAfterEventCoreAsync](M_Tessa_Cards_Numbers_NumberExtendable_NotifyAfterEventCoreAsync.htm)|
Выполняет постобработку события, происходящего с номером. Это предоставляет
возможность изменить результат обработанного события или сохранить результат
во внешнем хранилище.  
[NotifyBeforeEventAsync](M_Tessa_Cards_Numbers_NumberExtendable_NotifyBeforeEventAsync.htm)|
Выполняет предварительную обработку события, происходящего с номером. Это
предоставляет возможность полностью заместить или отменить стандартную
обработку.  
[NotifyBeforeEventCoreAsync](M_Tessa_Cards_Numbers_NumberExtendable_NotifyBeforeEventCoreAsync.htm)|
Выполняет предварительную обработку события, происходящего с номером. Это
предоставляет возможность полностью заместить или отменить стандартную
обработку.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[AfterEvent](E_Tessa_Cards_Numbers_NumberExtendable_AfterEvent.htm)|  Событие,
выполняемое в процессе постобработки события, происходящего с номером. Это
предоставляет возможность изменить результат обработанного события или
сохранить результат во внешнем хранилище.  
---|---  
[BeforeEvent](E_Tessa_Cards_Numbers_NumberExtendable_BeforeEvent.htm)|
Событие, выполняемое в процессе предварительной обработки события,
происходящего с номером. Это предоставляет возможность полностью заместить или
отменить стандартную обработку.  
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
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
