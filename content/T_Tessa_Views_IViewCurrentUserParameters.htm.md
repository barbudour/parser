# IViewCurrentUserParameters - интерфейс
Интерфейс представляющий доступ к параметрам CurrentUserId и текущей локали
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IViewCurrentUserParameters
VB __Копировать
     Public Interface IViewCurrentUserParameters
C++ __Копировать
     public interface class IViewCurrentUserParameters
F# __Копировать
     type IViewCurrentUserParameters = interface end
##  __Методы
[GetCurrentUserParameter(Boolean,
Boolean)](M_Tessa_Views_IViewCurrentUserParameters_GetCurrentUserParameter.htm)|
Создает и возвращает параметр текущий пользователь инициализированный
параметрами текущего пользователя  
---|---  
[GetCurrentUserParameter(Guid, String, Boolean,
Boolean)](M_Tessa_Views_IViewCurrentUserParameters_GetCurrentUserParameter_1.htm)|
Создает и возвращает параметр текущий пользователь  
[GetLocaleParameter](M_Tessa_Views_IViewCurrentUserParameters_GetLocaleParameter.htm)|
Создает и возвращает параметр Идентификатор культуры пользователя  
[ProvideCurrentUserIdParameter](M_Tessa_Views_IViewCurrentUserParameters_ProvideCurrentUserIdParameter.htm)|
Проставляет в список параметров значение текущего пользователя, если он там
отсутствует  
[ProvideLocaleParameter](M_Tessa_Views_IViewCurrentUserParameters_ProvideLocaleParameter.htm)|
Проставляет в список параметров идентификатор культуры. Если параметр уже есть
в списке он будет заменен  
## __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
