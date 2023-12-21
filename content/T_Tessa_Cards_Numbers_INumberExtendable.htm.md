# INumberExtendable - интерфейс
Объект, выполняющий расширяемые действия с номером.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INumberExtendable
VB __Копировать
     Public Interface INumberExtendable
C++ __Копировать
     public interface class INumberExtendable
F# __Копировать
     type INumberExtendable = interface end
##  __Методы
[NotifyAfterEventAsync](M_Tessa_Cards_Numbers_INumberExtendable_NotifyAfterEventAsync.htm)|
Выполняет постобработку события, происходящего с номером. Это предоставляет
возможность изменить результат обработанного события или сохранить результат
во внешнем хранилище.  
---|---  
[NotifyBeforeEventAsync](M_Tessa_Cards_Numbers_INumberExtendable_NotifyBeforeEventAsync.htm)|
Выполняет предварительную обработку события, происходящего с номером. Это
предоставляет возможность полностью заместить или отменить стандартную
обработку.  
## __События
[AfterEvent](E_Tessa_Cards_Numbers_INumberExtendable_AfterEvent.htm)|
Событие, выполняемое в процессе постобработки события, происходящего с
номером. Это предоставляет возможность изменить результат обработанного
события или сохранить результат во внешнем хранилище.  
---|---  
[BeforeEvent](E_Tessa_Cards_Numbers_INumberExtendable_BeforeEvent.htm)|
Событие, выполняемое в процессе предварительной обработки события,
происходящего с номером. Это предоставляет возможность полностью заместить или
отменить стандартную обработку.  
## __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
