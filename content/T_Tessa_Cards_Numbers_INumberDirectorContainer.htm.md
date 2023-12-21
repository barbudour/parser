# INumberDirectorContainer - интерфейс
Объект, выполняющий регистрацию и предоставляющий доступ к подсистеме номеров
для типов карточек, включая объекты
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm),
[INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm) и
[INumberQueueProcessor](T_Tessa_Cards_Numbers_INumberQueueProcessor.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INumberDirectorContainer
VB __Копировать
     Public Interface INumberDirectorContainer
C++ __Копировать
     public interface class INumberDirectorContainer
F# __Копировать
     type INumberDirectorContainer = interface end
##  __Методы
[GetProvider](M_Tessa_Cards_Numbers_INumberDirectorContainer_GetProvider.htm)|
Возвращает объект, предоставляющий доступ к объектам API номеров для заданного
типа карточки или для карточек всех типов по умолчанию.  
---|---  
[Register](M_Tessa_Cards_Numbers_INumberDirectorContainer_Register.htm)|
Регистрирует зависимости API номеров для всех типов карточек по умолчанию или
для типа карточки с указанным идентификатором.  
[Reset](M_Tessa_Cards_Numbers_INumberDirectorContainer_Reset.htm)|  Сбрасывает
все регистрации в объекте к состоянию по умолчанию. При этом объекта API
номеров запрашиваются из контейнера Unity по соответствующему интерфейсу.  
## __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
