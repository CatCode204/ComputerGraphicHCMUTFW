from Engine.Core.ApplicationCofiguration import ApplicationConfiguration

from TriangleApp import TriangleApp

appConfig = ApplicationConfiguration()
appConfig.WindowTitle = "RED TRIANGLE"

app = TriangleApp(appConfig).Run()