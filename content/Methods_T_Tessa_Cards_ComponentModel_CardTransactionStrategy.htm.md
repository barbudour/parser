# CardTransactionStrategy - методы
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[ExecuteInReaderLockAsync](M_Tessa_Cards_ComponentModel_CardTransactionStrategy_ExecuteInReaderLockAsync.htm)|
Выполняет запрос на чтение карточки внутри блокировки reader/writer.  
[ExecuteInTransactionAsync](M_Tessa_Platform_Data_TransactionStrategy_ExecuteInTransactionAsync.htm)|
Выполняет запрос на изменение карточки внутри транзакции. При этом не
используется блокировка reader/writer. Обычно транзакция открывается только в
том случае, если на этом соединении с БД отсутствует другая незакрытая
транзакция.  
(Унаследован от
[TransactionStrategy](T_Tessa_Platform_Data_TransactionStrategy.htm))  
[ExecuteInTransactionCoreAsync](M_Tessa_Platform_Data_TransactionStrategy_ExecuteInTransactionCoreAsync.htm)|
Выполняет запрос на изменение карточки внутри транзакции. При этом не
используется блокировка reader/writer. Обычно транзакция открывается только в
том случае, если на этом соединении с БД отсутствует другая незакрытая
транзакция.  
(Унаследован от
[TransactionStrategy](T_Tessa_Platform_Data_TransactionStrategy.htm))  
[ExecuteInWriterLockAsync](M_Tessa_Cards_ComponentModel_CardTransactionStrategy_ExecuteInWriterLockAsync.htm)|
Выполняет запрос на изменение карточки внутри блокировки reader/writer и
внутри транзакции. Последним действием внутри делегата asyncAction должно быть
увеличение номера версии карточки.  
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
[ProcessException](M_Tessa_Platform_Data_TransactionStrategy_ProcessException.htm)|
Записывает информацию по исключению, произошедшему в транзакции, в объект
validationResult.  
(Унаследован от
[TransactionStrategy](T_Tessa_Platform_Data_TransactionStrategy.htm))  
[ReleaseWriterLockAsync](M_Tessa_Cards_ComponentModel_CardTransactionStrategy_ReleaseWriterLockAsync.htm)|
Выполняет освобождение блокировки на запись карточки.  
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
[CardTransactionStrategy -
](T_Tessa_Cards_ComponentModel_CardTransactionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
