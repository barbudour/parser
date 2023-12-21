# CardPermissionInfo.CreateResolver - метод
Создаёт объект, осуществляющий поиск и кэширование прав доступа для полей и
строк.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardPermissionResolver CreateResolver()
VB __Копировать
     Public Function CreateResolver As ICardPermissionResolver
C++ __Копировать
     public:
    ICardPermissionResolver^ CreateResolver()
F# __Копировать
     member CreateResolver : unit -> ICardPermissionResolver 
#### Возвращаемое значение
[ICardPermissionResolver](T_Tessa_Cards_ICardPermissionResolver.htm)  
Объект, осуществляющий поиск и кэширование прав доступа для полей и строк.
##  __Заметки
В отличие от свойства
[Resolver](P_Tessa_Cards_CardPermissionInfo_Resolver.htm), метод всегда
возвращает новый экземпляр
[ICardPermissionResolver](T_Tessa_Cards_ICardPermissionResolver.htm), который
имеет собственный кэш.
## __См. также
#### Ссылки
[CardPermissionInfo - ](T_Tessa_Cards_CardPermissionInfo.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
