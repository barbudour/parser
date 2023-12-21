# CardTransactionParameter - свойства
##  __Свойства
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
## __См. также
#### Ссылки
[CardTransactionParameter -
](T_Tessa_Cards_ComponentModel_CardTransactionParameter.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
