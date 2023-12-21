# GrantAccess - класс
Вспомогательные методы для определения возможности представления доступов
## __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class GrantAccess
VB __Копировать
     Public NotInheritable Class GrantAccess
C++ __Копировать
     public ref class GrantAccess abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type GrantAccess = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ GrantAccess
##  __Методы
[MatchAllAsync<TAccessSubject,
TContext>](M_Tessa_Views_AccessPolicy_GrantAccess_MatchAllAsync__2.htm)|
Возвращает положительный ответ на запрос доступности если все правила доступа
вернули положительный ответ и в наличии есть хотя бы одно правило доступа  
---|---  
[MatchAllOrEmptyAsync<TAccessSubject,
TContext>](M_Tessa_Views_AccessPolicy_GrantAccess_MatchAllOrEmptyAsync__2.htm)|
Возвращает положительный ответ на запрос доступности если все правила доступа
вернули положительный ответ или правила доступа отсутствуют.  
[MatchAnyAsync<TAccessSubject,
TContext>](M_Tessa_Views_AccessPolicy_GrantAccess_MatchAnyAsync__2.htm)|
Возвращает положительный ответ на запрос доступности если хотя бы одно из
правил доступа вернуло положительный ответ.  
[MatchAnyOrEmptyAsync<TAccessSubject,
TContext>](M_Tessa_Views_AccessPolicy_GrantAccess_MatchAnyOrEmptyAsync__2.htm)|
Возвращает положительный ответ на запрос доступности если хотя бы одно из
правил доступа вернуло положительный ответ или правила доступа отсутствуют.  
## __См. также
#### Ссылки
[Tessa.Views.AccessPolicy - пространство имён](N_Tessa_Views_AccessPolicy.htm)
