# CardGetRestrictionValues - класс
Константы для флагов
[CardGetRestrictionFlags](T_Tessa_Cards_CardGetRestrictionFlags.htm),
ограничивающих загрузку информации для часто используемых сценариев.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardGetRestrictionValues
VB __Копировать
     Public NotInheritable Class CardGetRestrictionValues
C++ __Копировать
     public ref class CardGetRestrictionValues abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardGetRestrictionValues = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardGetRestrictionValues
##  __Поля
[AutoStartTasks](F_Tessa_Cards_CardGetRestrictionValues_AutoStartTasks.htm)|
Флаги, ограничивающие информацию, загружаемую в платформенной расширении при
наличии заданий с флагом [AutoStartTasks](T_Tessa_Cards_CardTypeFlags.htm).  
---|---  
[Backup](F_Tessa_Cards_CardGetRestrictionValues_Backup.htm)|  Флаги,
ограничивающие информацию, загружаемую при создании резервной копии для
восстановления карточки после удаления.  
[ContextRoles](F_Tessa_Cards_CardGetRestrictionValues_ContextRoles.htm)|
Флаги, ограничивающие информацию, загружаемую в кэш контекстных ролей.
Подразумевается, что контекстные роли не содержат файлов и заданий.  
[ExportAll](F_Tessa_Cards_CardGetRestrictionValues_ExportAll.htm)|  Флаги,
ограничивающие информацию, загружаемую при экспорте карточки, которая может
использоваться как для импорта, так и для создания по шаблону.  
[ExportForTemplate](F_Tessa_Cards_CardGetRestrictionValues_ExportForTemplate.htm)|
Флаги, ограничивающие информацию, загружаемую при экспорте карточки, которая
может использоваться только для создания по шаблону.  
[MainCardFromSatellite](F_Tessa_Cards_CardGetRestrictionValues_MainCardFromSatellite.htm)|
Флаги, ограничивающие информацию, загружаемую для основной карточки, которая
требуется для проверки прав при открытии из сателлита. При этом не загружаются
файлы, история заданий и информация по календарю для заданий.  
[Satellite](F_Tessa_Cards_CardGetRestrictionValues_Satellite.htm)|  Флаги,
ограничивающие информацию, загружаемую для карточек-сателлитов.
Подразумевается, что карточки-сателлиты не содержат файлов и заданий.  
[SatelliteWithFiles](F_Tessa_Cards_CardGetRestrictionValues_SatelliteWithFiles.htm)|
Флаги, ограничивающие информацию, загружаемую для карточек-сателлитов, которые
могут содержать файлы. Например, это сателлит карточки сотрудника,
используемый в web-клиенте для сохранения файла фонового изображения, которое
загрузил пользователь. Используйте флаги
[Satellite](F_Tessa_Cards_CardGetRestrictionValues_Satellite.htm) во всех
случаях, когда в таком сателлите файлы не нужны.  
[Singleton](F_Tessa_Cards_CardGetRestrictionValues_Singleton.htm)|  Флаги,
ограничивающие информацию, загружаемую для карточек-синглтонов.
Подразумевается, что карточки-синглтоны не содержат заданий.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
