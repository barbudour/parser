# ICardTransactionParameter - интерфейс
Параметр делегата выполняемой транзакции для карточек.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardTransactionParameter : ITransactionParameter
VB __Копировать
     Public Interface ICardTransactionParameter
    	Inherits ITransactionParameter
C++ __Копировать
     public interface class ICardTransactionParameter : ITransactionParameter
F# __Копировать
     type ICardTransactionParameter = 
        interface
            interface ITransactionParameter
        end
Implements
    [ITransactionParameter](T_Tessa_Platform_Data_ITransactionParameter.htm)
##  __Свойства
[CancellationToken](P_Tessa_Platform_Data_ITransactionParameter_CancellationToken.htm)|
Область видимости объекта [Tessa.Platform.Data.DbManager], внутри которой
выполняется транзакция. Обращение к свойствам объекта может привести к
фактическому созданию соединения с базой данных, если эмулируется отсутствие
транзакции. Гарантируется, что такое соединение будет корректно закрыто.  
(Унаследован от
[ITransactionParameter](T_Tessa_Platform_Data_ITransactionParameter.htm))  
---|---  
[CardID](P_Tessa_Cards_ComponentModel_ICardTransactionParameter_CardID.htm)|
Идентификатор карточки, для которой выполняется транзакция, или null, если
идентификатор карточки не проверяется.  
[CardTypeID](P_Tessa_Cards_ComponentModel_ICardTransactionParameter_CardTypeID.htm)|
Идентификатор типа карточки, для которой выполняется транзакция, или null,
если идентификатор неизвестен. Обычно идентификатор установлен для транзакции
на чтение карточки и равен null во всех остальных случаях.  
[DbScope](P_Tessa_Platform_Data_ITransactionParameter_DbScope.htm)|  Область
видимости объекта [Tessa.Platform.Data.DbManager], внутри которой выполняется
транзакция. Обращение к свойствам объекта может привести к фактическому
созданию соединения с базой данных, если эмулируется отсутствие транзакции.
Гарантируется, что такое соединение будет корректно закрыто.  
(Унаследован от
[ITransactionParameter](T_Tessa_Platform_Data_ITransactionParameter.htm))  
[ReportError](P_Tessa_Platform_Data_ITransactionParameter_ReportError.htm)|
Устанавливает или возвращает признак того, что при выполнении транзакции
возникла ошибка. Если была открыта транзакция, то её следует откатить. Если
при выполнении транзакции возникает исключение, то она откатывается
автоматически. По умолчанию возвращает значение false.  
(Унаследован от
[ITransactionParameter](T_Tessa_Platform_Data_ITransactionParameter.htm))  
[ValidationResult](P_Tessa_Platform_Data_ITransactionParameter_ValidationResult.htm)|
Результат валидации, связанный с открытой транзакцией.  
(Унаследован от
[ITransactionParameter](T_Tessa_Platform_Data_ITransactionParameter.htm))  
[Version](P_Tessa_Cards_ComponentModel_ICardTransactionParameter_Version.htm)|
Номер версии карточки, для которой должна быть открыта транзакция, или
[Tessa.Cards.ComponentModel.CardComponentHelper.DoNotCheckVersion], если
версия карточки не проверяется. Версия всегда не проверяется при чтении
карточки и может проверяться при изменении карточки.  
## __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
