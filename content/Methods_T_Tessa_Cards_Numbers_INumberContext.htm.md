# INumberContext - методы
##  __Методы
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
---|---  
##  __Методы расширения
[ExecuteNumberActionAsync](M_Tessa_Cards_Numbers_NumberExtensions_ExecuteNumberActionAsync.htm)|
Выполняет ранее установленное действие с номером по заданному ключу. Если
действие не было установлено, то возвращает false.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
---|---  
[Initialize](M_Tessa_Cards_Numbers_NumberExtensions_Initialize.htm)|
Выполняет инициализацию свойств для контекста действий с номером, если они не
были инициализированы:
[Director](P_Tessa_Cards_Numbers_INumberContext_Director.htm),
[Builder](P_Tessa_Cards_Numbers_INumberContext_Builder.htm) и
[EventType](P_Tessa_Cards_Numbers_INumberContext_EventType.htm). Инициализация
вызывается автоматически для вызова расширяемых методов
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm).  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[SetControl](M_Tessa_Cards_Numbers_NumberExtensions_SetControl.htm)|
Устанавливает в контексте элемент управления номерами, который инициировал
событие, происходящее с номером.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[SetControlLocation](M_Tessa_Cards_Numbers_NumberExtensions_SetControlLocation.htm)|
Устанавливает в контексте информацию по местоположению номера в карточке для
элемента управления номерами, который инициировал событие, происходящее с
номером.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[SetControlName](M_Tessa_Cards_Numbers_NumberExtensions_SetControlName.htm)|
Устанавливает в контексте имя элемента управления номерами, который
инициировал событие, происходящее с номером.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[SetNumberAction](M_Tessa_Cards_Numbers_NumberExtensions_SetNumberAction.htm)|
Устанавливает в контексте действие с номером, доступное по заданному ключу.
Значение null, переданное в параметр numberActionAsync, приводит к удалению
ранее заданного действия.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[TryGetControl<T>](M_Tessa_Cards_Numbers_NumberExtensions_TryGetControl__1.htm)|
Возвращает элемент управления номерами, который инициировал событие,
происходящее с номером, или null, если элемент управления неизвестен или если
его тип отличен от заданного.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[TryGetControlLocation](M_Tessa_Cards_Numbers_NumberExtensions_TryGetControlLocation.htm)|
Возвращает информацию по местоположению номера в карточке для элемента
управления номерами, который инициировал событие, происходящее с номером, или
null, если местоположение неизвестно.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[TryGetControlName](M_Tessa_Cards_Numbers_NumberExtensions_TryGetControlName.htm)|
Возвращает имя (алиас) элемента управления номерами, который инициировал
событие, происходящее с номером, или null, если элемент управления неизвестен
или если его тип отличен от заданного.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
##  __См. также
#### Ссылки
[INumberContext - ](T_Tessa_Cards_Numbers_INumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
