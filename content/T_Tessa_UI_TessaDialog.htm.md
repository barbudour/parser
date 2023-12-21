# TessaDialog - класс
Вспомогательный класс для отображения диалоговых окон.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static class TessaDialog
VB __Копировать
     Public NotInheritable Class TessaDialog
C++ __Копировать
     public ref class TessaDialog abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type TessaDialog = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TessaDialog
##  __Методы
[Confirm](M_Tessa_UI_TessaDialog_Confirm.htm)|  Отображает пользователю вопрос
в виде окна с сообщением и кнопками "Да" и "Нет".  
---|---  
[ConfirmAsync](M_Tessa_UI_TessaDialog_ConfirmAsync.htm)|  Отображает
пользователю вопрос в виде окна с сообщением и кнопками "Да" и "Нет". Вывод
выполняется всегда асинхронно в потоке UI, независимо от текущего потока.  
[ConfirmWithCancel](M_Tessa_UI_TessaDialog_ConfirmWithCancel.htm)|  Отображает
пользователю вопрос в виде окна с сообщением и кнопками "Да", "Нет" и
"Отмена".  
[ConfirmWithCancelAsync](M_Tessa_UI_TessaDialog_ConfirmWithCancelAsync.htm)|
Отображает пользователю вопрос в виде окна с сообщением и кнопками "Да", "Нет"
и "Отмена". Вывод выполняется всегда асинхронно в потоке UI, независимо от
текущего потока.  
[ShowError](M_Tessa_UI_TessaDialog_ShowError.htm)|  Отображает пользователю
окно с сообщением об ошибке.  
[ShowErrorAsync](M_Tessa_UI_TessaDialog_ShowErrorAsync.htm)|  Отображает
пользователю окно с сообщением об ошибке. Вывод выполняется всегда асинхронно
в потоке UI, независимо от текущего потока.  
[ShowException](M_Tessa_UI_TessaDialog_ShowException.htm)|  Отображает
исключение в окне сообщений.  
[ShowExceptionAsync](M_Tessa_UI_TessaDialog_ShowExceptionAsync.htm)|
Отображает исключение в окне сообщений. Вывод выполняется всегда асинхронно в
потоке UI, независимо от текущего потока.  
[ShowMessage](M_Tessa_UI_TessaDialog_ShowMessage.htm)|  Отображает
пользователю окно с сообщением.  
[ShowMessageAsync](M_Tessa_UI_TessaDialog_ShowMessageAsync.htm)|  Отображает
пользователю окно с сообщением. Вывод выполняется всегда асинхронно в потоке
UI, независимо от текущего потока.  
[ShowNotEmpty(IValidationResultBuilder, String, Boolean,
TessaDialogDispatcher, Boolean)](M_Tessa_UI_TessaDialog_ShowNotEmpty.htm)|
Отображает результат валидации в окне сообщений.  
[ShowNotEmpty(ValidationResult, String, Boolean, TessaDialogDispatcher,
Boolean)](M_Tessa_UI_TessaDialog_ShowNotEmpty_1.htm)|  Отображает результат
валидации в окне сообщений.  
[ShowNotEmptyAsync(IValidationResultBuilder, String, Boolean, Boolean,
Boolean)](M_Tessa_UI_TessaDialog_ShowNotEmptyAsync.htm)|  Отображает результат
валидации в окне сообщений. Вывод выполняется всегда асинхронно в потоке UI,
независимо от текущего потока.  
[ShowNotEmptyAsync(ValidationResult, String, Boolean, Boolean,
Boolean)](M_Tessa_UI_TessaDialog_ShowNotEmptyAsync_1.htm)|  Отображает
результат валидации в окне сообщений. Вывод выполняется всегда асинхронно в
потоке UI, независимо от текущего потока.  
## __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
