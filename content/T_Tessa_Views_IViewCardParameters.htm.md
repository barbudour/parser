# IViewCardParameters - интерфейс
Интерфейс представляющий доступ к формированию специальных параметров типа и
идентификатора карточки
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IViewCardParameters
VB __Копировать
     Public Interface IViewCardParameters
C++ __Копировать
     public interface class IViewCardParameters
F# __Копировать
     type IViewCardParameters = interface end
##  __Методы
[GetCardIdParameter](M_Tessa_Views_IViewCardParameters_GetCardIdParameter.htm)|
Создает и возвращает параметр Идентификатор текущей карточки  
---|---  
[GetCardTypeIdParameter](M_Tessa_Views_IViewCardParameters_GetCardTypeIdParameter.htm)|
Создает и возвращает параметр идентификатор типа текущей карточки  
[ProvideCurrentCardIdParameter](M_Tessa_Views_IViewCardParameters_ProvideCurrentCardIdParameter.htm)|
Проставлеяет в список параметров идентификатор текущей карточки. Если параметр
уже есть в списке он будет заменен  
[ProvideCurrentCardTypeIdParameter](M_Tessa_Views_IViewCardParameters_ProvideCurrentCardTypeIdParameter.htm)|
Проставляет в список параметров идентификатор типа текущей карточки. Если
параметр уже есть в списке он будет заменен.  
## __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
