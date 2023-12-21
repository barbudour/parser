# NumberContext - методы
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
[Seal](M_Tessa_Cards_Numbers_NumberContext_Seal.htm)| Защищает объект от
изменений.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[ExecuteNumberActionAsync](M_Tessa_Cards_Numbers_NumberExtensions_ExecuteNumberActionAsync.htm)|
Выполняет ранее установленное действие с номером по заданному ключу. Если
действие не было установлено, то возвращает false.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Initialize](M_Tessa_Cards_Numbers_NumberExtensions_Initialize.htm)|
Выполняет инициализацию свойств для контекста действий с номером, если они не
были инициализированы:
[Director](P_Tessa_Cards_Numbers_INumberContext_Director.htm),
[Builder](P_Tessa_Cards_Numbers_INumberContext_Builder.htm) и
[EventType](P_Tessa_Cards_Numbers_INumberContext_EventType.htm). Инициализация
вызывается автоматически для вызова расширяемых методов
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm).  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
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
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
