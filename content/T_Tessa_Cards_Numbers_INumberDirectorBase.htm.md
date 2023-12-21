# INumberDirectorBase - интерфейс
Базовый интерфейс для объектов, реализующих произвольное взаимодействие с
номерами карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INumberDirectorBase : INumberExtendable, 
    	ISealable
VB __Копировать
     Public Interface INumberDirectorBase
    	Inherits INumberExtendable, ISealable
C++ __Копировать
     public interface class INumberDirectorBase : INumberExtendable, 
    	ISealable
F# __Копировать
     type INumberDirectorBase = 
        interface
            interface INumberExtendable
            interface ISealable
        end
Implements
    [INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[AvailableEventTypes](P_Tessa_Cards_Numbers_INumberDirectorBase_AvailableEventTypes.htm)|
Доступные типы событий, происходящие с номерами. Изменение этой коллекции
позволяет отключить обработку некоторых событий для всех карточек, к которым
применим текущий объект.  
---|---  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
##  __Методы
[GetBuilder](M_Tessa_Cards_Numbers_INumberDirectorBase_GetBuilder.htm)|
Возвращает объект, осуществляющий низкоуровневые действия с номерами, которые
зависят от бизнес-логики. Не возвращает null.  
---|---  
[IsAvailableAsync](M_Tessa_Cards_Numbers_INumberDirectorBase_IsAvailableAsync.htm)|
Выполняет проверку доступности для типа события, происходящего с номером.  
[NotifyAfterEventAsync](M_Tessa_Cards_Numbers_INumberExtendable_NotifyAfterEventAsync.htm)|
Выполняет постобработку события, происходящего с номером. Это предоставляет
возможность изменить результат обработанного события или сохранить результат
во внешнем хранилище.  
(Унаследован от
[INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm))  
[NotifyBeforeEventAsync](M_Tessa_Cards_Numbers_INumberExtendable_NotifyBeforeEventAsync.htm)|
Выполняет предварительную обработку события, происходящего с номером. Это
предоставляет возможность полностью заместить или отменить стандартную
обработку.  
(Унаследован от
[INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm))  
[NotifyOnEventAsync](M_Tessa_Cards_Numbers_INumberDirectorBase_NotifyOnEventAsync.htm)|
Выполняет заданное действие с номером.  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
##  __События
[AfterEvent](E_Tessa_Cards_Numbers_INumberExtendable_AfterEvent.htm)|
Событие, выполняемое в процессе постобработки события, происходящего с
номером. Это предоставляет возможность изменить результат обработанного
события или сохранить результат во внешнем хранилище.  
(Унаследован от
[INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm))  
---|---  
[BeforeEvent](E_Tessa_Cards_Numbers_INumberExtendable_BeforeEvent.htm)|
Событие, выполняемое в процессе предварительной обработки события,
происходящего с номером. Это предоставляет возможность полностью заместить или
отменить стандартную обработку.  
(Унаследован от
[INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm))  
##  __Методы расширения
[EnsureAvailable](M_Tessa_Cards_Numbers_NumberExtensions_EnsureAvailable.htm)|
Гарантирует, что объект INumberDirectorBase в коллекции доступных типов
событий
[AvailableEventTypes](P_Tessa_Cards_Numbers_INumberDirectorBase_AvailableEventTypes.htm)
будет содержать тип действия eventType. Если коллекция защищена от изменений и
тип события в ней отсутствовал, то метод возвращает false.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
