import gpxpy
import gpxpy.gpx
import datetime

# Creating a new file:
# --------------------

gpx = gpxpy.gpx.GPX()

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

# Create points:
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1234, 5.1234, name='我的測試', time=datetime.datetime.fromtimestamp(1552851007.22396), elevation=1234))
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1235, 5.1235, name='我的測試', time=datetime.datetime.fromtimestamp(1552851007.22396), elevation=1235))
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1236, 5.1236, name='我的測試', time=datetime.datetime.fromtimestamp(1552851007.22396), elevation=1236))

# You can add routes and waypoints, too...

print('Created GPX:', gpx.to_xml())
