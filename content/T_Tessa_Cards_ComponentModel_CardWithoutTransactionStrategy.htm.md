# CardWithoutTransactionStrategy - класс
Стратегия неблокирующего выполнения операций с карточкой. Взятие и
освобождение любых блокировок reader/writer не выполняется, транзакции не
используются.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class CardWithoutTransactionStrategy : WithoutTransactionStrategy, 
    	ICardTransactionStrategy, ITransactionStrategy
VB __Копировать
     Public Class CardWithoutTransactionStrategy
    	Inherits WithoutTransactionStrategy
    	Implements ICardTransactionStrategy, ITransactionStrategy
C++ __Копировать
     public ref class CardWithoutTransactionStrategy : public WithoutTransactionStrategy, 
    	ICardTransactionStrategy, ITransactionStrategy
F# __Копировать
     type CardWithoutTransactionStrategy = 
        class
            inherit WithoutTransactionStrategy
            interface ICardTransactionStrategy
            interface ITransactionStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[TransactionStrategy](T_Tessa_Platform_Data_TransactionStrategy.htm) __[WithoutTransactionStrategy](T_Tessa_Platform_Data_WithoutTransactionStrategy.htm) __ CardWithoutTransactionStrategy
Implements
    [ICardTransactionStrategy](T_Tessa_Cards_ComponentModel_ICardTransactionStrategy.htm), [ITransactionStrategy](T_Tessa_Platform_Data_ITransactionStrategy.htm)
##  __Заметки
Наследники класса могут определять дополнительные свойства и методы, а также
переопределять существующие методы.
## __Конструкторы
[CardWithoutTransactionStrategy](M_Tessa_Cards_ComponentModel_CardWithoutTransactionStrategy__ctor.htm)|
Создаёт экземпляр класса с указанием области видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).  
---|---  
## __Свойства
[CardWithoutLockingStrategy](P_Tessa_Cards_ComponentModel_CardWithoutTransactionStrategy_CardWithoutLockingStrategy.htm)|
Стратегия по блокировкам карточек. Используется только при взятии блокировки
на чтение для получения идентификатора типа карточки.  
---|---  
[DbScope](P_Tessa_Platform_Data_TransactionStrategy_DbScope.htm)|  Объект,
обеспечивающий взаимодействие с базой данных.  
(Унаследован от
[TransactionStrategy](T_Tessa_Platform_Data_TransactionStrategy.htm))  
[TransactionScope](P_Tessa_Platform_Data_TransactionStrategy_TransactionScope.htm)|
Объект для управления областью выполнения транзакции.  
(Унаследован от
[TransactionStrategy](T_Tessa_Platform_Data_TransactionStrategy.htm))  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[ExecuteInReaderLockAsync](M_Tessa_Cards_ComponentModel_CardWithoutTransactionStrategy_ExecuteInReaderLockAsync.htm)|
Выполняет запрос на чтение карточки внутри блокировки reader/writer.  
[ExecuteInTransactionAsync](M_Tessa_Platform_Data_TransactionStrategy_ExecuteInTransactionAsync.htm)|
Выполняет запрос на изменение карточки внутри транзакции. При этом не
используется блокировка reader/writer. Обычно транзакция открывается только в
том случае, если на этом соединении с БД отсутствует другая незакрытая
транзакция.  
(Унаследован от
[TransactionStrategy](T_Tessa_Platform_Data_TransactionStrategy.htm))  
[ExecuteInTransactionCoreAsync](M_Tessa_Platform_Data_WithoutTransactionStrategy_ExecuteInTransactionCoreAsync.htm)|
Выполняет запрос на изменение карточки внутри транзакции. При этом не
используется блокировка reader/writer. Обычно транзакция открывается только в
том случае, если на этом соединении с БД отсутствует другая незакрытая
транзакция.  
(Унаследован от
[WithoutTransactionStrategy](T_Tessa_Platform_Data_WithoutTransactionStrategy.htm))  
[ExecuteInWriterLockAsync](M_Tessa_Cards_ComponentModel_CardWithoutTransactionStrategy_ExecuteInWriterLockAsync.htm)|
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
[ReleaseWriterLockAsync](M_Tessa_Cards_ComponentModel_CardWithoutTransactionStrategy_ReleaseWriterLockAsync.htm)|
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
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
