# CardLockingStrategy - свойства
##  __Свойства
[ConfigurationInfoProvider](P_Tessa_Cards_CardLockingStrategy_ConfigurationInfoProvider.htm)|
Провайдер информации о конфигурации.  
---|---  
[DbScope](P_Tessa_Cards_CardLockingStrategy_DbScope.htm)|  Объект,
обеспечивающий взаимодействие с базой данных.  
[ObtainLockCommandTimeoutSeconds](P_Tessa_Cards_CardLockingStrategy_ObtainLockCommandTimeoutSeconds.htm)|
Таймаут на выполнение команд взятия блокировок в секундах. При таком таймауте
блокировка может быть взята в БД, но не взята с точки зрения сервера .NET.
Берём 15 минут, а не бесконечность, на случай, когда сервер СУБД безвозвратно
упал.  
[ReleaseLockCommandTimeoutSeconds](P_Tessa_Cards_CardLockingStrategy_ReleaseLockCommandTimeoutSeconds.htm)|
Таймаут на снятие блокировок в секундах. Берём 5 минут, а не бесконечность, на
случай, когда сервер СУБД безвозвратно упал.  
[Session](P_Tessa_Cards_CardLockingStrategy_Session.htm)|  Сессия для текущего
пользователя.  
## __См. также
#### Ссылки
[CardLockingStrategy - ](T_Tessa_Cards_CardLockingStrategy.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
