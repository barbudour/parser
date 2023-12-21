# INumberDirectorBase - методы
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
##  __Методы расширения
[EnsureAvailable](M_Tessa_Cards_Numbers_NumberExtensions_EnsureAvailable.htm)|
Гарантирует, что объект
[INumberDirectorBase](T_Tessa_Cards_Numbers_INumberDirectorBase.htm) в
коллекции доступных типов событий
[AvailableEventTypes](P_Tessa_Cards_Numbers_INumberDirectorBase_AvailableEventTypes.htm)
будет содержать тип действия eventType. Если коллекция защищена от изменений и
тип события в ней отсутствовал, то метод возвращает false.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[INumberDirectorBase - ](T_Tessa_Cards_Numbers_INumberDirectorBase.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
