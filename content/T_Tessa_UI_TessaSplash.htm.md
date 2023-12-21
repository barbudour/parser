# TessaSplash - класс
Вспомогательный класс для создания операций ожидания.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static class TessaSplash
VB __Копировать
     Public NotInheritable Class TessaSplash
C++ __Копировать
     public ref class TessaSplash abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type TessaSplash = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TessaSplash
##  __Методы
[CollapseAll](M_Tessa_UI_TessaSplash_CollapseAll.htm)|  Временно скрывает все
активные окна-заставки при их наличии и восстанавливает их, когда вызван
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) у возвращённого объекта. Вызов
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) обязателен, поэтому рекомендуется заключить возвращённый
результат в using. Допустимы вложенные вызовы этого метода, причём только
самый первый вызов выполняет действия.  
---|---  
[Create(String, Func<Window>, Int32)](M_Tessa_UI_TessaSplash_Create.htm)|
Создаёт окно-заставку, информирующую пользователя о выполнении длительной
операции.  
[Create(TessaSplashMessage, Func<Window>,
Int32)](M_Tessa_UI_TessaSplash_Create_1.htm)|  Создаёт окно-заставку,
информирующую пользователя о выполнении длительной операции.  
[CreateLauncher](M_Tessa_UI_TessaSplash_CreateLauncher.htm)|  Создаёт окно-
заставку с крупным изображением на белом фоне, обычно отображаемую при запуске
приложения.  
[CreateLazy(Func<ValueTuple<String, Boolean>,
ISplash>)](M_Tessa_UI_TessaSplash_CreateLazy_1.htm)|  Создаёт окно-заставку,
информирующую пользователя о выполнении длительной операции, которая создаётся
отложенно при изменении свойства [Text](P_Tessa_Platform_ISplash_Text.htm).  
[CreateLazy(Func<Window>, Int32)](M_Tessa_UI_TessaSplash_CreateLazy.htm)|
Создаёт окно-заставку, информирующую пользователя о выполнении длительной
операции, которая создаётся отложенно при изменении свойства
[Text](P_Tessa_Platform_ISplash_Text.htm).  
[GetMessage](M_Tessa_UI_TessaSplash_GetMessage.htm)|  Возвращает стандартное
сообщение для вывода окна-заставки в виде текста. Обычно возвращается строка
локализации вида $LocalizationString  
[QuietMode](M_Tessa_UI_TessaSplash_QuietMode.htm)|  Временно включает "тихий"
режим, при котором не один из сплэшей не отображается на экране.
Восстанавливает создание и вывод сплэшей, когда вызван
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) у возвращённого объекта.  
## __Поля
[DefaultDelay](F_Tessa_UI_TessaSplash_DefaultDelay.htm)|  Задержка по
умолчанию в миллисекундах перед отображением экранов загрузки. Не относится к
экрану загрузки приложения, созданному посредством [CreateLauncher(Uri,
String, String, Boolean, Boolean, Boolean, Nullable<Color>,
Nullable<Color>)](M_Tessa_UI_TessaSplash_CreateLauncher.htm).  
---|---  
## __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
