# IViewSpecialParameters - интерфейс
Интерфейс для предоставления методов внедрения специальных параметров
Представлений в список параметров
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IViewSpecialParameters : IViewPagingParameters, 
    	IViewCardParameters, IViewCurrentUserParameters
VB __Копировать
     Public Interface IViewSpecialParameters
    	Inherits IViewPagingParameters, IViewCardParameters, IViewCurrentUserParameters
C++ __Копировать
     public interface class IViewSpecialParameters : IViewPagingParameters, 
    	IViewCardParameters, IViewCurrentUserParameters
F# __Копировать
     type IViewSpecialParameters = 
        interface
            interface IViewPagingParameters
            interface IViewCardParameters
            interface IViewCurrentUserParameters
        end
Implements
    [IViewCardParameters](T_Tessa_Views_IViewCardParameters.htm), [IViewCurrentUserParameters](T_Tessa_Views_IViewCurrentUserParameters.htm), [IViewPagingParameters](T_Tessa_Views_IViewPagingParameters.htm)
##  __Методы
[GetCardIdParameter](M_Tessa_Views_IViewCardParameters_GetCardIdParameter.htm)|
Создает и возвращает параметр Идентификатор текущей карточки  
(Унаследован от [IViewCardParameters](T_Tessa_Views_IViewCardParameters.htm))  
---|---  
[GetCardTypeIdParameter](M_Tessa_Views_IViewCardParameters_GetCardTypeIdParameter.htm)|
Создает и возвращает параметр идентификатор типа текущей карточки  
(Унаследован от [IViewCardParameters](T_Tessa_Views_IViewCardParameters.htm))  
[GetCurrentUserParameter(Boolean,
Boolean)](M_Tessa_Views_IViewCurrentUserParameters_GetCurrentUserParameter.htm)|
Создает и возвращает параметр текущий пользователь инициализированный
параметрами текущего пользователя  
(Унаследован от
[IViewCurrentUserParameters](T_Tessa_Views_IViewCurrentUserParameters.htm))  
[GetCurrentUserParameter(Guid, String, Boolean,
Boolean)](M_Tessa_Views_IViewCurrentUserParameters_GetCurrentUserParameter_1.htm)|
Создает и возвращает параметр текущий пользователь  
(Унаследован от
[IViewCurrentUserParameters](T_Tessa_Views_IViewCurrentUserParameters.htm))  
[GetLocaleParameter](M_Tessa_Views_IViewCurrentUserParameters_GetLocaleParameter.htm)|
Создает и возвращает параметр Идентификатор культуры пользователя  
(Унаследован от
[IViewCurrentUserParameters](T_Tessa_Views_IViewCurrentUserParameters.htm))  
[GetPageLimitParameter](M_Tessa_Views_IViewPagingParameters_GetPageLimitParameter.htm)|
Создает и возвращает параметр пейджинга - количество отображаемых данных  
(Унаследован от
[IViewPagingParameters](T_Tessa_Views_IViewPagingParameters.htm))  
[GetPageOffsetParameter](M_Tessa_Views_IViewPagingParameters_GetPageOffsetParameter.htm)|
Создает и возвращает параметр пейджинга - смешение внутри списка  
(Унаследован от
[IViewPagingParameters](T_Tessa_Views_IViewPagingParameters.htm))  
[ProvideCurrentCardIdParameter](M_Tessa_Views_IViewCardParameters_ProvideCurrentCardIdParameter.htm)|
Проставлеяет в список параметров идентификатор текущей карточки. Если параметр
уже есть в списке он будет заменен  
(Унаследован от [IViewCardParameters](T_Tessa_Views_IViewCardParameters.htm))  
[ProvideCurrentCardTypeIdParameter](M_Tessa_Views_IViewCardParameters_ProvideCurrentCardTypeIdParameter.htm)|
Проставляет в список параметров идентификатор типа текущей карточки. Если
параметр уже есть в списке он будет заменен.  
(Унаследован от [IViewCardParameters](T_Tessa_Views_IViewCardParameters.htm))  
[ProvideCurrentUserIdParameter](M_Tessa_Views_IViewCurrentUserParameters_ProvideCurrentUserIdParameter.htm)|
Проставляет в список параметров значение текущего пользователя, если он там
отсутствует  
(Унаследован от
[IViewCurrentUserParameters](T_Tessa_Views_IViewCurrentUserParameters.htm))  
[ProvideLocaleParameter](M_Tessa_Views_IViewCurrentUserParameters_ProvideLocaleParameter.htm)|
Проставляет в список параметров идентификатор культуры. Если параметр уже есть
в списке он будет заменен  
(Унаследован от
[IViewCurrentUserParameters](T_Tessa_Views_IViewCurrentUserParameters.htm))  
[ProvidePageLimitParameter](M_Tessa_Views_IViewPagingParameters_ProvidePageLimitParameter.htm)|
Проставляет в список параметров значение для параметра PageLimit  
(Унаследован от
[IViewPagingParameters](T_Tessa_Views_IViewPagingParameters.htm))  
[ProvidePageOffsetParameter](M_Tessa_Views_IViewPagingParameters_ProvidePageOffsetParameter.htm)|
Проставляет в список параметров значение для параметра PageOffset  
(Унаследован от
[IViewPagingParameters](T_Tessa_Views_IViewPagingParameters.htm))  
##  __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
