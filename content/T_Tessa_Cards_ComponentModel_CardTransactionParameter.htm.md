# CardTransactionParameter - класс
Реализация параметра делегата выполняемой транзакции для карточек.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class CardTransactionParameter : TransactionParameter, 
    	ICardTransactionParameter, ITransactionParameter
VB __Копировать
     Public Class CardTransactionParameter
    	Inherits TransactionParameter
    	Implements ICardTransactionParameter, ITransactionParameter
C++ __Копировать
     public ref class CardTransactionParameter : public TransactionParameter, 
    	ICardTransactionParameter, ITransactionParameter
F# __Копировать
     type CardTransactionParameter = 
        class
            inherit TransactionParameter
            interface ICardTransactionParameter
            interface ITransactionParameter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[TransactionParameter](T_Tessa_Platform_Data_TransactionParameter.htm) __ CardTransactionParameter
Implements
    [ICardTransactionParameter](T_Tessa_Cards_ComponentModel_ICardTransactionParameter.htm), [ITransactionParameter](T_Tessa_Platform_Data_ITransactionParameter.htm)
##  __Заметки
Наследники класса могут добавить дополнительные свойства.
## __Конструкторы
[CardTransactionParameter](M_Tessa_Cards_ComponentModel_CardTransactionParameter__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[CancellationToken](P_Tessa_Platform_Data_TransactionParameter_CancellationToken.htm)|
Область видимости объекта [Tessa.Platform.Data.DbManager], внутри которой
выполняется транзакция. Обращение к свойствам объекта может привести к
фактическому созданию соединения с базой данных, если эмулируется отсутствие
транзакции. Гарантируется, что такое соединение будет корректно закрыто.  
(Унаследован от
[TransactionParameter](T_Tessa_Platform_Data_TransactionParameter.htm))  
---|---  
[CardID](P_Tessa_Cards_ComponentModel_CardTransactionParameter_CardID.htm)|
Идентификатор карточки, для которой выполняется транзакция, или null, если
идентификатор карточки не проверяется.  
[CardTypeID](P_Tessa_Cards_ComponentModel_CardTransactionParameter_CardTypeID.htm)|
Идентификатор типа карточки, для которой выполняется транзакция, или null,
если идентификатор неизвестен. Обычно идентификатор установлен для транзакции
на чтение карточки и равен null во всех остальных случаях.  
[DbScope](P_Tessa_Platform_Data_TransactionParameter_DbScope.htm)|  Область
видимости объекта [Tessa.Platform.Data.DbManager], внутри которой выполняется
транзакция. Обращение к свойствам объекта может привести к фактическому
созданию соединения с базой данных, если эмулируется отсутствие транзакции.
Гарантируется, что такое соединение будет корректно закрыто.  
(Унаследован от
[TransactionParameter](T_Tessa_Platform_Data_TransactionParameter.htm))  
[ReportError](P_Tessa_Platform_Data_TransactionParameter_ReportError.htm)|
Устанавливает или возвращает признак того, что при выполнении транзакции
возникла ошибка. Если была открыта транзакция, то её следует откатить. Если
при выполнении транзакции возникает исключение, то она откатывается
автоматически. По умолчанию возвращает значение false.  
(Унаследован от
[TransactionParameter](T_Tessa_Platform_Data_TransactionParameter.htm))  
[ValidationResult](P_Tessa_Platform_Data_TransactionParameter_ValidationResult.htm)|
Результат валидации, связанный с открытой транзакцией.  
(Унаследован от
[TransactionParameter](T_Tessa_Platform_Data_TransactionParameter.htm))  
[Version](P_Tessa_Cards_ComponentModel_CardTransactionParameter_Version.htm)|
Номер версии карточки, для которой должна быть открыта транзакция, или
[Tessa.Cards.ComponentModel.CardComponentHelper.DoNotCheckVersion], если
версия карточки не проверяется. Версия всегда не проверяется при чтении
карточки и может проверяться при изменении карточки.  
## __Методы
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
