# INumberDirectorProvider - интерфейс
Объект, предоставляющий доступ к подсистеме номеров для типов карточек,
включая объекты [INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm),
[INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm) и
[INumberQueueProcessor](T_Tessa_Cards_Numbers_INumberQueueProcessor.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INumberDirectorProvider
VB __Копировать
     Public Interface INumberDirectorProvider
C++ __Копировать
     public interface class INumberDirectorProvider
F# __Копировать
     type INumberDirectorProvider = interface end
##  __Методы
[GetComposer](M_Tessa_Cards_Numbers_INumberDirectorProvider_GetComposer.htm)|
Возвращает объект, обрабатывающий логику выделения и изменения номеров
карточек.  
---|---  
[GetDirector](M_Tessa_Cards_Numbers_INumberDirectorProvider_GetDirector.htm)|
Возвращает объект, управляющий взаимодействием с номерами карточек.  
[GetQueueProcessor](M_Tessa_Cards_Numbers_INumberDirectorProvider_GetQueueProcessor.htm)|
Возвращает объект, выполняющий обработку действий в очереди с номерами.  
##  __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
