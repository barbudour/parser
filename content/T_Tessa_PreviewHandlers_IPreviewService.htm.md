# IPreviewService - интерфейс
Сервис для взаимодействия с приложениями, осуществляющими отображение файлов в
предварительном просмотре.
## __Definition
 **Пространство имён:** [Tessa.PreviewHandlers](N_Tessa_PreviewHandlers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPreviewService
VB __Копировать
     Public Interface IPreviewService
C++ __Копировать
     public interface class IPreviewService
F# __Копировать
     type IPreviewService = interface end
##  __Методы
[DoPreviewAsync](M_Tessa_PreviewHandlers_IPreviewService_DoPreviewAsync.htm)|
Осуществляет запуск предварительного просмотра и возвращает результат запуска.
Если значение result вернуло false, то запуск не поддерживается и значение
exceptionText может содержать текст исключения, если он доступен. Если
значение result вернуло true, то текст исключения всегда равен null.  
---|---  
[SetFileAsync](M_Tessa_PreviewHandlers_IPreviewService_SetFileAsync.htm)|
Устанавливает путь к файлу и возвращает результат запуска. Если значение
result вернуло false, то запуск не поддерживается и значение exceptionText
может содержать текст исключения, если он доступен. Если значение result
вернуло true, то текст исключения всегда равен null.  
[SetFocusAsync](M_Tessa_PreviewHandlers_IPreviewService_SetFocusAsync.htm)|
Устанавливает фокус  
[SetPreviewAreaAsync](M_Tessa_PreviewHandlers_IPreviewService_SetPreviewAreaAsync.htm)|
Осуществляет установку позиции элемента отображающего файл относительно окна
приложения  
[SetPreviewAreaWindowAsync](M_Tessa_PreviewHandlers_IPreviewService_SetPreviewAreaWindowAsync.htm)|
Устанавливает указатель окна и область в которой требуется отобразить просмотр
файла.  
[UnloadAsync](M_Tessa_PreviewHandlers_IPreviewService_UnloadAsync.htm)|
Осуществляет выгрузку приложения  
## __См. также
#### Ссылки
[Tessa.PreviewHandlers - пространство имён](N_Tessa_PreviewHandlers.htm)
